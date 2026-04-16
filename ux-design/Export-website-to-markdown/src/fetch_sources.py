#!/usr/bin/env python3
"""
Fetch external source articles referenced in growth.design/psychology biases.

Reads the parsed JSON data, downloads each external URL,
converts to Markdown, and saves locally.

Outputs:
  - output/sources/{domain}/{slug}_{hash}.md
  - output/sources_index.md
"""

import json
import os
import re
import time
import urllib.parse
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import html2text

from config import (
    OUTPUT_DIR, SOURCES_DIR, SOURCES_INDEX_FILE,
    SOURCE_FETCH_DELAY, SOURCE_FETCH_TIMEOUT, USER_AGENT,
)
from utils import clean_text, slugify, hash_url


# Domains to skip (internal or non-article links)
SKIP_DOMAINS = {
    'growth.design',
    'twitter.com',
    'x.com',
    'linkedin.com',
    'facebook.com',
    'youtube.com',
    'youtu.be',
    'github.com',
    'apps.apple.com',
    'play.google.com',
    'mailto:',
    'tel:',
}

# Domains that typically block scrapers
LIKELY_PAYWALL = {
    'medium.com',
    'hbr.org',
    'wsj.com',
    'nytimes.com',
}


def collect_urls(data):
    """Collect all unique external URLs from the parsed data."""
    urls = set()

    # From allLinks
    for link in data.get('allLinks', []):
        url = link.get('url', '')
        if url:
            urls.add(url)

    # From bias sources
    for cat in data.get('categories', []):
        for bias in cat.get('biases', []):
            for src in bias.get('sources', []):
                url = src.get('url', '')
                if url:
                    urls.add(url)

    # From resources
    for res in data.get('resources', []):
        url = res.get('url', '')
        if url:
            urls.add(url)

    return urls


def should_fetch(url):
    """Check if a URL should be fetched (external article, not social media, etc.)."""
    if not url or not url.startswith('http'):
        return False

    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()

    # Remove www prefix for matching
    if domain.startswith('www.'):
        domain = domain[4:]

    for skip in SKIP_DOMAINS:
        if skip in domain:
            return False

    return True


def get_domain(url):
    """Extract the domain from a URL."""
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain


def get_filename(url):
    """Generate a safe filename from a URL."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip('/')
    if path:
        slug = slugify(path.split('/')[-1] or path.replace('/', '-'))
    else:
        slug = 'index'
    # Truncate slug to avoid too-long filenames
    slug = slug[:80]
    url_hash = hash_url(url)
    return f"{slug}_{url_hash}.md"


def extract_article_content(html_content, url):
    """Extract main article content from HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove noise
    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer',
                               'aside', 'iframe', 'noscript', 'form']):
        tag.decompose()

    for el in soup.find_all(class_=re.compile(
        r'nav|menu|sidebar|footer|header|cookie|banner|popup|modal|ad[s_-]|share|social|comment',
        re.I
    )):
        el.decompose()

    # Try to find the main article content
    main_content = None
    for selector in [
        ('article', {}),
        ('main', {}),
        ('div', {'class': re.compile(r'article|post|content|entry', re.I)}),
        ('div', {'role': 'main'}),
        ('div', {'id': re.compile(r'article|post|content|main', re.I)}),
    ]:
        main_content = soup.find(selector[0], selector[1])
        if main_content:
            break

    if not main_content:
        main_content = soup.find('body') or soup

    # Get title
    title = ''
    title_el = soup.find('title')
    if title_el:
        title = title_el.get_text(strip=True)
    h1 = soup.find('h1')
    if h1:
        title = h1.get_text(strip=True)

    # Convert to Markdown using html2text
    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = True
    converter.ignore_emphasis = False
    converter.body_width = 0  # Don't wrap lines
    converter.unicode_snob = True
    converter.skip_internal_links = True

    markdown_content = converter.handle(str(main_content))

    return title, markdown_content


def fetch_url(url, session):
    """Fetch a single URL and return (status, title, markdown_content)."""
    domain = get_domain(url)

    try:
        response = session.get(url, timeout=SOURCE_FETCH_TIMEOUT, allow_redirects=True)

        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'text/html' not in content_type and 'application/xhtml' not in content_type:
                return ('skip', f'Non-HTML content: {content_type}', '', '')

            title, markdown = extract_article_content(response.text, url)
            return ('ok', '', title, markdown)

        elif response.status_code == 403:
            return ('blocked', f'403 Forbidden (likely paywall)', '', '')
        elif response.status_code == 404:
            return ('not_found', '404 Not Found', '', '')
        elif response.status_code == 429:
            return ('rate_limited', '429 Rate Limited', '', '')
        else:
            return ('error', f'HTTP {response.status_code}', '', '')

    except requests.exceptions.Timeout:
        return ('timeout', 'Request timed out', '', '')
    except requests.exceptions.ConnectionError as e:
        return ('error', f'Connection error: {e}', '', '')
    except Exception as e:
        return ('error', f'Unexpected error: {e}', '', '')


def save_source(url, title, markdown, domain):
    """Save a fetched source as a Markdown file."""
    domain_dir = SOURCES_DIR / domain
    domain_dir.mkdir(parents=True, exist_ok=True)

    filename = get_filename(url)
    filepath = domain_dir / filename

    content = f"# {title}\n\n"
    content += f"*Source: [{url}]({url})*\n\n"
    content += f"---\n\n"
    content += clean_text(markdown)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def build_sources_index(results):
    """Build a Markdown index of all fetched sources."""
    md = []
    now = datetime.now().strftime('%Y-%m-%d')

    md.append("# Sources Index — growth.design/psychology")
    md.append("")
    md.append(f"*Generated: {now}*")
    md.append("")

    # Summary stats
    total = len(results)
    ok = sum(1 for r in results if r['status'] == 'ok')
    blocked = sum(1 for r in results if r['status'] == 'blocked')
    not_found = sum(1 for r in results if r['status'] == 'not_found')
    errors = sum(1 for r in results if r['status'] in ('error', 'timeout', 'rate_limited'))
    skipped = sum(1 for r in results if r['status'] == 'skip')

    md.append("## Summary")
    md.append("")
    md.append(f"| Status | Count |")
    md.append(f"|--------|-------|")
    md.append(f"| Downloaded | {ok} |")
    md.append(f"| Blocked/Paywall | {blocked} |")
    md.append(f"| Not Found (404) | {not_found} |")
    md.append(f"| Errors | {errors} |")
    md.append(f"| Skipped (non-HTML) | {skipped} |")
    md.append(f"| **Total** | **{total}** |")
    md.append("")

    # Group by domain
    by_domain = {}
    for r in results:
        d = r['domain']
        if d not in by_domain:
            by_domain[d] = []
        by_domain[d].append(r)

    md.append("## Sources by Domain")
    md.append("")

    for domain in sorted(by_domain.keys()):
        items = by_domain[domain]
        md.append(f"### {domain}")
        md.append("")
        for item in items:
            status = item['status']
            url = item['url']
            title = item.get('title', '')
            local = item.get('local_path', '')

            if status == 'ok' and local:
                rel_path = os.path.relpath(local, OUTPUT_DIR)
                md.append(f"- [{title or url}]({rel_path}) — [Original]({url})")
            elif status == 'blocked':
                md.append(f"- [{title or url}]({url}) — *Blocked (paywall/403)*")
            elif status == 'not_found':
                md.append(f"- [{url}]({url}) — *Not Found (404)*")
            else:
                note = item.get('note', status)
                md.append(f"- [{url}]({url}) — *{note}*")
        md.append("")

    return '\n'.join(md)


def main():
    print("=" * 60)
    print("Fetching External Sources")
    print("=" * 60)

    # Load parsed data
    parsed_json = OUTPUT_DIR / "growth_design_psychology_parsed.json"
    if not parsed_json.exists():
        # Fall back to raw data
        parsed_json = OUTPUT_DIR / "growth_design_psychology_data.json"

    if not parsed_json.exists():
        print("ERROR: No data file found. Run scrape_psychology.py and convert_to_markdown.py first.")
        return

    print(f"\nLoading data from {parsed_json}...")
    with open(parsed_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Collect unique URLs
    all_urls = collect_urls(data)
    print(f"Found {len(all_urls)} total URLs")

    # Filter to external fetchable URLs
    fetch_urls = [url for url in all_urls if should_fetch(url)]
    print(f"URLs to fetch: {len(fetch_urls)}")

    if not fetch_urls:
        print("No external URLs to fetch.")
        return

    # Setup HTTP session
    session = requests.Session()
    session.headers.update({
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    })

    # Create output directory
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch each URL
    results = []
    for i, url in enumerate(sorted(fetch_urls), 1):
        domain = get_domain(url)
        print(f"\n[{i}/{len(fetch_urls)}] {domain}: {url[:80]}...")

        status, note, title, markdown = fetch_url(url, session)

        result = {
            'url': url,
            'domain': domain,
            'status': status,
            'note': note,
            'title': title,
            'local_path': '',
        }

        if status == 'ok' and markdown:
            filepath = save_source(url, title, markdown, domain)
            result['local_path'] = str(filepath)
            file_size = filepath.stat().st_size
            print(f"  OK: {title[:60]} ({file_size / 1024:.1f} KB)")
        else:
            print(f"  {status.upper()}: {note}")

        results.append(result)

        # Rate limiting
        time.sleep(SOURCE_FETCH_DELAY)

    # Build sources index
    print("\nBuilding sources index...")
    index_md = build_sources_index(results)
    with open(SOURCES_INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(index_md)

    # Save results as JSON too (for debugging)
    results_json = OUTPUT_DIR / "sources_fetch_results.json"
    with open(results_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    # Summary
    ok = sum(1 for r in results if r['status'] == 'ok')
    print(f"\n{'=' * 60}")
    print("FETCH COMPLETE")
    print(f"Downloaded: {ok}/{len(results)} sources")
    print(f"Index: {SOURCES_INDEX_FILE}")
    print(f"Sources dir: {SOURCES_DIR}")
    print("=" * 60)


if __name__ == '__main__':
    main()
