#!/usr/bin/env python3
"""
Convert growth.design/psychology snapshot into structured Markdown.

Parses the Playwright accessibility snapshot (snapshot_expanded.md) which has
a clean, structured representation of the fully-expanded page.

Outputs:
  - output/growth_design_psychology.md  (main Markdown file)
  - output/growth_design_psychology_parsed.json  (structured JSON for fetch_sources.py)
"""

import json
import re
from datetime import datetime
from pathlib import Path

from config import OUTPUT_DIR, MARKDOWN_FILE, TARGET_URL
from utils import clean_text, slugify

SNAPSHOT_FILE = OUTPUT_DIR / "snapshot_expanded.md"
PARSED_JSON = OUTPUT_DIR / "growth_design_psychology_parsed.json"

# Category markers in the snapshot
CATEGORY_MARKERS = {
    '🙈 Information': {
        'name': 'Information',
        'emoji': '🙈',
        'description': 'Users filter out a lot of the information that they receive, even when it could be important.',
    },
    '🔮 Meaning': {
        'name': 'Meaning',
        'emoji': '🔮',
        'description': 'When users try to give sense to information, they make stories and assumptions to fill the gaps.',
    },
    '⏰ Time': {
        'name': 'Time',
        'emoji': '⏰',
        'description': 'Users are busy so they look for shortcuts and jump to conclusions quickly.',
    },
    '💾 Memory': {
        'name': 'Memory',
        'emoji': '💾',
        'description': 'Users try to remember what\'s most important, but their brain prefers some elements over others.',
    },
}


def parse_snapshot():
    """Parse the Playwright snapshot to extract all biases and resources."""
    with open(SNAPSHOT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    categories = []
    resources = []
    current_category = None
    current_bias = None
    current_section = None  # 'definition', 'examples', 'checklist', 'sources'
    resource_mode = False
    cheat_sheet_text = []
    nir_quote = ''
    in_cheat_sheet = False
    in_nir_quote = False

    # State for parsing
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        stripped = line.strip()

        # Detect category headers
        for marker, info in CATEGORY_MARKERS.items():
            if stripped.startswith('- paragraph') and i + 1 < len(lines):
                # Check if next meaningful content is the category marker
                pass
            if f': {marker}' in stripped or stripped == f'- text: {marker}':
                if current_bias:
                    if current_category:
                        current_category['biases'].append(current_bias)
                    current_bias = None
                if current_category:
                    categories.append(current_category)
                current_category = {
                    'name': info['name'],
                    'emoji': info['emoji'],
                    'description': info['description'],
                    'biases': [],
                }
                resource_mode = False
                break

        # Detect "Product Psychology Resources" heading
        if 'Product Psychology Resources' in stripped:
            if current_bias:
                if current_category:
                    current_category['biases'].append(current_bias)
                current_bias = None
            if current_category:
                categories.append(current_category)
                current_category = None
            resource_mode = True

        # Detect cheat sheet section
        if 'Cognitive Biases Cheat sheet' in stripped:
            resource_mode = False
            in_cheat_sheet = True

        # Detect Nir Eyal quote
        if '"We all have a responsibility to build ethically' in stripped:
            nir_quote = stripped.strip('- text: ').strip('"').strip("'")
            # Read until we find the attribution
            j = i + 1
            while j < len(lines) and '— Nir Eyal' not in lines[j]:
                quote_line = lines[j].strip().strip('- text: ').strip('"').strip("'")
                if quote_line and not quote_line.startswith(('generic', 'blockquote', 'img')):
                    nir_quote += ' ' + quote_line
                j += 1
            if j < len(lines) and '— Nir Eyal' in lines[j]:
                nir_quote_attr = lines[j].strip()
                # Extract attribution
                attr_match = re.search(r'(— Nir Eyal.*?)(?:\]|$)', nir_quote_attr)
                if attr_match:
                    nir_quote += '\n\n' + attr_match.group(1)

        # Detect h2 headings (bias titles)
        h2_match = re.match(r'\s*- heading "(.*?)" \[level=2\]', stripped)
        if h2_match:
            title = h2_match.group(1)

            # Skip non-bias headings
            if title in ('Share the knowledge with your colleagues.',):
                i += 1
                continue

            # Look ahead for emoji (previous line) and description (next paragraph)
            emoji = ''
            # Look backwards for emoji
            for back in range(max(0, i - 5), i):
                back_line = lines[back].strip()
                emoji_match = re.search(
                    r'generic \[ref=\w+\]: ([\U0001F300-\U0001F9FF\U00002600-\U000027BF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U0000FE00-\U0000FE0F\u200d\U0001F1E0-\U0001F1FF\u2600-\u26FF\u2700-\u27BF]+)',
                    back_line
                )
                if emoji_match:
                    emoji = emoji_match.group(1)
                    break

            # Look ahead for short description paragraph
            description = ''
            for fwd in range(i + 1, min(i + 5, len(lines))):
                fwd_line = lines[fwd].strip()
                desc_match = re.match(r'- paragraph \[ref=\w+\]: "(.*)"', fwd_line)
                if not desc_match:
                    desc_match = re.match(r'- paragraph \[ref=\w+\]: (.*)', fwd_line)
                if desc_match:
                    description = desc_match.group(1).strip('"').strip("'")
                    break

            # Look ahead for "Coming Soon" or "Collapse ↑" or "Expand ↓"
            is_coming_soon = False
            is_expanded = False
            for fwd in range(i + 1, min(i + 8, len(lines))):
                fwd_line = lines[fwd].strip()
                if 'Coming Soon' in fwd_line:
                    is_coming_soon = True
                    break
                if 'Collapse' in fwd_line:
                    is_expanded = True
                    break

            # Save previous bias
            if current_bias:
                if resource_mode:
                    resources.append(current_bias)
                elif current_category:
                    current_category['biases'].append(current_bias)

            current_bias = {
                'emoji': emoji,
                'title': title,
                'description': description,
                'is_coming_soon': is_coming_soon,
                'definition': '',
                'examples': [],
                'checklist': [],
                'sources': [],
            }
            current_section = None

        # Detect h3 headings (definition, examples, checklist sections)
        h3_match = re.match(r'\s*- heading "(.*?)" \[level=3\]', stripped)
        if h3_match and current_bias:
            section_title = h3_match.group(1).lower()
            if 'definition' in section_title or 'description' in section_title:
                current_section = 'definition'
            elif 'example' in section_title:
                current_section = 'examples'
            elif 'checklist' in section_title:
                current_section = 'checklist'
            else:
                current_section = None

        # Extract paragraph content
        para_match = re.match(r'\s*- paragraph \[ref=\w+\]: "(.*)"', stripped)
        if not para_match:
            para_match = re.match(r'\s*- paragraph \[ref=\w+\]: (.*)', stripped)
        if para_match and current_bias and current_section:
            text = para_match.group(1).strip('"').strip("'")
            if current_section == 'definition':
                if current_bias['definition']:
                    current_bias['definition'] += '\n\n' + text
                else:
                    current_bias['definition'] = text
            elif current_section == 'examples':
                current_bias['examples'].append({'text': text, 'links': []})
            elif current_section == 'checklist':
                current_bias['checklist'].append(text)

        # Extract inline text (- text: ...)
        text_match = re.match(r'\s*- text: (.*)', stripped)
        if text_match and current_bias and current_section:
            text = text_match.group(1).strip('"').strip("'")
            if current_section == 'definition':
                if current_bias['definition']:
                    current_bias['definition'] += ' ' + text
                else:
                    current_bias['definition'] = text
            elif current_section == 'examples' and current_bias['examples']:
                current_bias['examples'][-1]['text'] += ' ' + text

        # Extract links
        link_match = re.match(r'\s*- link "(.*?)" \[ref=\w+\]', stripped)
        if link_match and current_bias:
            link_text = link_match.group(1)
            # Get URL from next line
            url = ''
            if i + 1 < len(lines):
                url_match = re.match(r'\s*- /url: (.*)', lines[i + 1].strip())
                if url_match:
                    url = url_match.group(1).strip()
                    if url.startswith('/'):
                        url = 'https://growth.design' + url

            if current_section == 'examples' and current_bias['examples']:
                current_bias['examples'][-1]['links'].append({'text': link_text, 'url': url})

        # Extract listitem content (for checklist and sources)
        listitem_match = re.match(r'\s*- listitem \[ref=\w+\]: (.*)', stripped)
        if listitem_match and current_bias:
            text = listitem_match.group(1).strip('"').strip("'")
            if current_section == 'checklist':
                current_bias['checklist'].append(text)

        # Detect source links (list items with links at the end of a bias section)
        # Sources are typically in a list right before the next bias starts
        # They follow the pattern: listitem > link with URL
        if (link_match and current_bias and not current_section
                and not is_case_study_link(link_match.group(1))):
            link_text = link_match.group(1)
            url = ''
            if i + 1 < len(lines):
                url_match = re.match(r'\s*- /url: (.*)', lines[i + 1].strip())
                if url_match:
                    url = url_match.group(1).strip()
                    if url.startswith('/'):
                        url = 'https://growth.design' + url
            if url and not url.startswith('https://growth.design/case-studies'):
                current_bias['sources'].append({'text': link_text, 'url': url})

        i += 1

    # Don't forget the last bias
    if current_bias:
        if resource_mode:
            resources.append(current_bias)
        elif current_category:
            current_category['biases'].append(current_bias)

    if current_category:
        categories.append(current_category)

    return categories, resources, nir_quote


def is_case_study_link(text):
    """Check if a link text looks like a case study card (not a source reference)."""
    return ('Case Study Tile' in text or
            'Growth.Design Case Study' in text or
            len(text) > 100)


def parse_sources_from_snapshot():
    """Second pass: extract source links that appear at the end of each expanded bias.

    Source lists in the snapshot have a distinctive pattern:
    - They're in a `list [ref=...]` element
    - Each listitem contains a single `link` to an external URL
    - The link text typically contains author/publisher and year
    - They appear AFTER the examples/checklist sections (no h3 heading above them)
    """
    with open(SNAPSHOT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sources_by_bias = {}
    current_bias_title = None
    current_section = None  # Track which h3 section we're in

    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        # Track current bias (h2)
        h2_match = re.match(r'- heading "(.*?)" \[level=2\]', stripped)
        if h2_match:
            current_bias_title = h2_match.group(1)
            current_section = None

        # Track h3 sections
        h3_match = re.match(r'- heading "(.*?)" \[level=3\]', stripped)
        if h3_match:
            title = h3_match.group(1).lower()
            if 'definition' in title or 'description' in title:
                current_section = 'definition'
            elif 'example' in title:
                current_section = 'examples'
            elif 'checklist' in title:
                current_section = 'checklist'
            else:
                current_section = 'other'

        # Detect source list: a `list` element followed by listitem > link patterns
        # Source lists are NOT preceded by an h3 heading (they're standalone)
        list_match = re.match(r'\s*- list \[ref=\w+\]:', stripped)
        if list_match and current_bias_title:
            # Look ahead: is this a source list?
            # A source list has listitem children that each contain a link to an external URL
            # and NO paragraphs or images
            j = i + 1
            candidate_sources = []
            is_source_list = True
            has_paragraph = False

            while j < len(lines):
                sj = lines[j].strip()

                # Stop at same or lower indentation (end of list)
                if sj and not sj.startswith('-'):
                    break
                # Check indentation - if we go back to list level or higher, stop
                line_indent = len(lines[j]) - len(lines[j].lstrip())
                list_indent = len(lines[i]) - len(lines[i].lstrip())
                if sj.startswith('- ') and line_indent <= list_indent and j > i + 1:
                    break

                # Check for paragraph (means this is an examples list, not sources)
                if re.match(r'\s*- paragraph', sj):
                    has_paragraph = True
                    break
                if re.match(r'\s*- img', sj):
                    has_paragraph = True
                    break

                # Extract links
                link_match = re.match(r'\s*-\s*(?:\')?link "(.*?)" \[ref=\w+\]', sj)
                if link_match:
                    link_text = link_match.group(1)
                    # Get URL
                    if j + 1 < len(lines):
                        url_match = re.match(r'\s*- /url: (.*)', lines[j + 1].strip())
                        if url_match:
                            url = url_match.group(1).strip()
                            if url.startswith('/'):
                                url = 'https://growth.design' + url
                            candidate_sources.append({'text': link_text, 'url': url})

                j += 1

            # A source list has: links but no paragraphs/images, and the links
            # go to external URLs (not case studies)
            if candidate_sources and not has_paragraph:
                external_sources = []
                for src in candidate_sources:
                    url = src['url']
                    text = src['text']
                    if (not url.startswith('https://growth.design/case-studies')
                            and not url.startswith('https://growth.design/psychology')
                            and 'Case Study Tile' not in text
                            and 'Growth.Design Case Study' not in text
                            and len(text) < 200):
                        external_sources.append(src)

                if external_sources:
                    if current_bias_title not in sources_by_bias:
                        sources_by_bias[current_bias_title] = []
                    sources_by_bias[current_bias_title].extend(external_sources)

        i += 1

    return sources_by_bias


def build_markdown(categories, resources, nir_quote):
    """Build the final Markdown document."""
    md = []
    now = datetime.now().strftime('%Y-%m-%d')

    # Title
    md.append("# 🧠 106 Cognitive Biases & Principles That Affect Your UX")
    md.append("")
    md.append(f"*Source: [{TARGET_URL}]({TARGET_URL})*")
    md.append(f"*Exported: {now}*")
    md.append("")
    md.append("Every time users interact with your product, they:")
    md.append("- 🙈 Filter the **information**")
    md.append("- 🔮 Seek the **meaning** of it")
    md.append("- ⏰ Act within a given **time**")
    md.append("- 💾 Store bits of the interaction in their **memories**")
    md.append("")
    md.append("---")
    md.append("")

    # Table of Contents
    md.append("## Table of Contents")
    md.append("")

    total_biases = 0
    total_expanded = 0
    total_coming_soon = 0

    for cat in categories:
        cat_slug = slugify(cat['name'])
        bias_count = len(cat['biases'])
        total_biases += bias_count
        md.append(f"- [{cat['emoji']} {cat['name']}](#{cat_slug}) ({bias_count} biases)")
        for bias in cat['biases']:
            bias_slug = slugify(bias['title'])
            emoji = bias.get('emoji', '')
            title = bias['title']
            if bias.get('is_coming_soon'):
                md.append(f"  - [{emoji} {title}](#{bias_slug}) *(Coming Soon)*")
                total_coming_soon += 1
            else:
                md.append(f"  - [{emoji} {title}](#{bias_slug})")
                total_expanded += 1

    if resources:
        md.append(f"- [📚 Resources](#resources) ({len(resources)} items)")
    md.append("- [📋 Cheat Sheet](#cognitive-biases-cheat-sheet)")
    md.append("")
    md.append(f"**Total: {total_biases} cognitive biases** ({total_expanded} expanded, {total_coming_soon} coming soon)")
    md.append("")
    md.append("---")
    md.append("")

    # Categories and biases
    for cat in categories:
        md.append(f"## {cat['emoji']} {cat['name']}")
        md.append("")
        md.append(f"*{cat['description']}*")
        md.append("")

        for bias in cat['biases']:
            emoji = bias.get('emoji', '')
            title = bias['title']
            md.append(f"### {emoji} {title}")
            md.append("")

            if bias.get('description'):
                md.append(f"> {bias['description']}")
                md.append("")

            if bias.get('is_coming_soon'):
                md.append("*Coming Soon*")
                md.append("")
                md.append("---")
                md.append("")
                continue

            if bias.get('definition'):
                md.append("#### Definition")
                md.append("")
                md.append(clean_text(bias['definition']))
                md.append("")

            if bias.get('examples'):
                md.append("#### Examples")
                md.append("")
                for j, ex in enumerate(bias['examples'], 1):
                    text = ex if isinstance(ex, str) else ex.get('text', '')
                    links = [] if isinstance(ex, str) else ex.get('links', [])
                    md.append(f"{j}. {text}")
                    for link in links:
                        if link.get('url') and 'Case Study Tile' not in link.get('text', ''):
                            md.append(f"   - [{link['text']}]({link['url']})")
                md.append("")

            if bias.get('checklist'):
                md.append("#### Checklist")
                md.append("")
                for item in bias['checklist']:
                    md.append(f"- [ ] {item}")
                md.append("")

            if bias.get('sources'):
                md.append("#### Sources")
                md.append("")
                for src in bias['sources']:
                    text = src.get('text', src.get('url', ''))
                    url = src.get('url', '')
                    if url:
                        md.append(f"- [{text}]({url})")
                    else:
                        md.append(f"- {text}")
                md.append("")

            md.append("---")
            md.append("")

    # Resources section
    if resources:
        md.append("## 📚 Resources")
        md.append("")
        md.append("If you want to learn more about **behavioral psychology and mental models**, we recommend these resources:")
        md.append("")

        for res in resources:
            emoji = res.get('emoji', '📖')
            title = res.get('title', '')
            desc = res.get('description', '')
            md.append(f"### {emoji} {title}")
            md.append("")
            if desc:
                md.append(f"> {desc}")
                md.append("")
            if res.get('definition'):
                md.append(clean_text(res['definition']))
                md.append("")
            if res.get('sources'):
                for src in res['sources']:
                    md.append(f"- [{src['text']}]({src['url']})")
                md.append("")
            md.append("---")
            md.append("")

    # Cheat Sheet section
    md.append("## 📋 Cognitive Biases Cheat Sheet")
    md.append("")
    md.append("We took the time to summarize each principle in one line.")
    md.append("Use it as a user empathy reminder while you build a feature.")
    md.append("")

    # Quick reference table
    md.append("| # | Bias | Summary |")
    md.append("|---|------|---------|")
    num = 1
    for cat in categories:
        for bias in cat['biases']:
            emoji = bias.get('emoji', '')
            title = bias['title']
            desc = bias.get('description', '')
            status = ' *(Soon)*' if bias.get('is_coming_soon') else ''
            md.append(f"| {num} | {emoji} {title}{status} | {desc} |")
            num += 1
    md.append("")

    # Nir Eyal quote
    if nir_quote:
        md.append("---")
        md.append("")
        md.append(f"> {nir_quote}")
        md.append("")

    # Footer
    md.append("---")
    md.append("")
    md.append(f"*Generated from [growth.design/psychology]({TARGET_URL}) on {now}*")
    md.append("")

    return '\n'.join(md)


def main():
    print("=" * 60)
    print("Converting growth.design/psychology to Markdown")
    print("=" * 60)

    if not SNAPSHOT_FILE.exists():
        print(f"ERROR: Snapshot file not found: {SNAPSHOT_FILE}")
        print("Run scrape_psychology.py first to generate the snapshot.")
        return

    # Parse snapshot
    print("\nParsing snapshot...")
    categories, resources, nir_quote = parse_snapshot()

    # Parse sources separately (more reliable second pass)
    print("Extracting source references...")
    sources_by_bias = parse_sources_from_snapshot()

    # Merge sources into biases
    for cat in categories:
        for bias in cat['biases']:
            extra_sources = sources_by_bias.get(bias['title'], [])
            # Deduplicate by URL
            existing_urls = {s['url'] for s in bias.get('sources', [])}
            for src in extra_sources:
                if src['url'] not in existing_urls:
                    bias['sources'].append(src)
                    existing_urls.add(src['url'])

    for res in resources:
        extra_sources = sources_by_bias.get(res['title'], [])
        existing_urls = {s['url'] for s in res.get('sources', [])}
        for src in extra_sources:
            if src['url'] not in existing_urls:
                res['sources'].append(src)

    # Stats
    total_biases = sum(len(c['biases']) for c in categories)
    expanded = sum(1 for c in categories for b in c['biases'] if not b.get('is_coming_soon'))
    coming_soon = sum(1 for c in categories for b in c['biases'] if b.get('is_coming_soon'))
    total_sources = sum(len(b.get('sources', [])) for c in categories for b in c['biases'])
    print(f"Found {len(categories)} categories with {total_biases} biases")
    print(f"  Expanded: {expanded}")
    print(f"  Coming Soon: {coming_soon}")
    print(f"  Resources: {len(resources)}")
    print(f"  Source links: {total_sources}")

    # Build Markdown
    print("\nBuilding Markdown...")
    markdown = build_markdown(categories, resources, nir_quote)

    # Write Markdown
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown)

    file_size = MARKDOWN_FILE.stat().st_size
    print(f"\nOutput: {MARKDOWN_FILE}")
    print(f"Size: {file_size / 1024:.1f} KB")

    # Save parsed data as JSON for fetch_sources.py
    all_links = []
    for cat in categories:
        for bias in cat['biases']:
            for src in bias.get('sources', []):
                all_links.append(src)
            for ex in bias.get('examples', []):
                if isinstance(ex, dict):
                    for link in ex.get('links', []):
                        all_links.append(link)

    parsed_data = {
        'categories': categories,
        'resources': resources,
        'allLinks': all_links,
    }
    with open(PARSED_JSON, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=2)
    print(f"Parsed data: {PARSED_JSON}")

    print(f"\n{'=' * 60}")
    print("CONVERSION COMPLETE")
    print(f"Next step: python fetch_sources.py")
    print("=" * 60)


if __name__ == '__main__':
    main()
