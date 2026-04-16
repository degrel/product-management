#!/usr/bin/env python3
"""
Scrape growth.design/psychology — expand all collapsible sections and extract structured data.

Uses Playwright with a persistent Chrome profile (inherits logged-in session).
Outputs JSON to output/growth_design_psychology_data.json.
"""

import json
import time
import sys
from pathlib import Path

from config import (
    TARGET_URL, OUTPUT_DIR, DATA_FILE,
    CHROME_USER_DATA_DIR, CHROME_PROFILE,
    CLICK_DELAY_MS, EXPAND_TIMEOUT_MS, PAGE_LOAD_TIMEOUT_MS, MAX_RETRIES,
)

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed. Run: pip install playwright && python -m playwright install chromium")
    sys.exit(1)


def launch_browser(playwright):
    """Launch Chromium with persistent Chrome profile for auth."""
    user_data = str(CHROME_USER_DATA_DIR)
    print(f"Using Chrome profile: {user_data} / {CHROME_PROFILE}")

    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data,
        channel="chrome",
        headless=False,
        args=[f"--profile-directory={CHROME_PROFILE}"],
        timeout=PAGE_LOAD_TIMEOUT_MS,
    )
    return context


def expand_all_sections(page):
    """Click every 'Expand' button on the page."""
    # Find all expand buttons
    expand_buttons = page.locator('button:has-text("Expand"), [role="button"]:has-text("Expand")')
    count = expand_buttons.count()
    print(f"Found {count} expandable sections")

    if count == 0:
        # Try alternative selectors
        expand_buttons = page.locator('[data-state="closed"]')
        count = expand_buttons.count()
        print(f"Fallback: found {count} closed sections")

    expanded = 0
    for i in range(count):
        btn = expand_buttons.nth(i)
        try:
            # Check if this button is actually an expand trigger
            text = btn.inner_text()
            if "coming soon" in text.lower():
                continue

            btn.scroll_into_view_if_needed()
            btn.click()
            time.sleep(CLICK_DELAY_MS / 1000)

            expanded += 1
            if expanded % 10 == 0:
                print(f"  Expanded {expanded} sections...")

        except Exception as e:
            print(f"  Warning: could not expand section {i}: {e}")
            continue

    print(f"Expanded {expanded} sections total")
    return expanded


def extract_data(page):
    """Extract all bias data from the fully-expanded page using page.evaluate()."""
    data = page.evaluate("""() => {
        const result = {
            title: '',
            description: '',
            categories: [],
            resources: [],
            cheatSheet: null,
            citation: null,
            extractedAt: new Date().toISOString(),
            sourceUrl: window.location.href
        };

        // Page title & description
        const h1 = document.querySelector('h1');
        if (h1) result.title = h1.innerText.trim();

        const heroDesc = document.querySelector('[class*="hero"] p, [class*="subtitle"]');
        if (heroDesc) result.description = heroDesc.innerText.trim();

        // Locate category sections
        // growth.design uses sections with category headers (Information, Meaning, Time, Memory)
        const allSections = document.querySelectorAll('section, [class*="category"], [class*="section"]');

        // Helper: extract links from an element
        function extractLinks(el) {
            if (!el) return [];
            const links = [];
            el.querySelectorAll('a[href]').forEach(a => {
                const href = a.getAttribute('href');
                if (href && !href.startsWith('#') && !href.startsWith('javascript:')) {
                    links.push({
                        text: a.innerText.trim(),
                        url: href.startsWith('/') ? 'https://growth.design' + href : href
                    });
                }
            });
            return links;
        }

        // Helper: extract checklist items
        function extractChecklist(el) {
            if (!el) return [];
            const items = [];
            el.querySelectorAll('li, [class*="check"]').forEach(li => {
                const text = li.innerText.trim();
                if (text) items.push(text);
            });
            return items;
        }

        // Try to find cognitive bias cards/items
        // Each bias typically has: emoji, title, short description, and optionally expanded content
        const biasCards = document.querySelectorAll(
            '[class*="bias"], [class*="card"], [class*="accordion"], [class*="item"], [class*="cognitive"]'
        );

        // Group biases by finding category headers
        const categoryNames = ['Information', 'Meaning', 'Time', 'Memory', 'Resources'];
        let currentCategory = null;
        const categoryMap = {};

        // Walk through the DOM to find categories and their biases
        const mainContent = document.querySelector('main, [class*="main"], [class*="content"], body');
        if (!mainContent) return result;

        // Get all headings that might be categories
        const headings = mainContent.querySelectorAll('h2, h3, [class*="category-title"], [class*="heading"]');
        headings.forEach(h => {
            const text = h.innerText.trim();
            for (const cat of categoryNames) {
                if (text.includes(cat)) {
                    categoryMap[cat] = {
                        name: cat,
                        fullTitle: text,
                        element: h,
                        biases: []
                    };
                }
            }
        });

        // If we couldn't find categories via headings, just collect all biases flat
        if (Object.keys(categoryMap).length === 0) {
            categoryMap['All'] = { name: 'All', fullTitle: 'All Cognitive Biases', biases: [] };
        }

        // Now extract individual bias items
        // Look for elements that seem like individual bias entries
        const allElements = mainContent.querySelectorAll('*');
        let currentCat = Object.keys(categoryMap)[0];
        const processedTitles = new Set();

        for (const el of allElements) {
            // Check if this element is a category header
            if (el.tagName.match(/^H[23]$/) || el.className?.includes?.('category')) {
                const text = el.innerText.trim();
                for (const cat of Object.keys(categoryMap)) {
                    if (text.includes(cat)) {
                        currentCat = cat;
                        break;
                    }
                }
            }
        }

        // Alternative approach: serialize the entire visible page content for post-processing
        // This captures everything regardless of DOM structure
        const pageContent = {
            html: mainContent.innerHTML,
            text: mainContent.innerText,
            allLinks: extractLinks(mainContent)
        };

        result.pageContent = pageContent;

        // Also try to extract structured data from any JSON-LD or data attributes
        const jsonLd = document.querySelectorAll('script[type="application/ld+json"]');
        const structuredData = [];
        jsonLd.forEach(script => {
            try {
                structuredData.push(JSON.parse(script.textContent));
            } catch(e) {}
        });
        if (structuredData.length > 0) {
            result.structuredData = structuredData;
        }

        // Extract categories with their descriptions
        result.categories = Object.values(categoryMap).map(cat => ({
            name: cat.name,
            fullTitle: cat.fullTitle,
            biases: cat.biases
        }));

        return result;
    }""")
    return data


def extract_detailed_biases(page):
    """Second pass: extract each bias card with full detail."""
    data = page.evaluate("""() => {
        const biases = [];

        // The page structure: each cognitive bias is typically in an accordion-like element
        // After expanding, the full content is visible

        // Strategy: find all elements that look like bias titles (emoji + name pattern)
        // Then extract the content that follows each title

        // Look for common patterns in growth.design's DOM
        // Try multiple selector strategies

        const selectors = [
            // Accordion items
            '[class*="accordion"] > div, [class*="accordion"] > li',
            // Card-based layout
            '[class*="bias-card"], [class*="BiasCard"], [class*="bias_card"]',
            // Generic expandable items
            '[class*="collapsible"], [class*="expandable"]',
            // Data attributes
            '[data-bias], [data-cognitive]',
            // Radix/headless UI accordion patterns (common in Next.js sites)
            '[data-state="open"], [data-radix-collection-item]',
            // Generic item containers
            '[class*="item-content"], [class*="ItemContent"]',
        ];

        let items = [];
        for (const sel of selectors) {
            const found = document.querySelectorAll(sel);
            if (found.length > 5) {  // likely the right selector if many matches
                items = found;
                break;
            }
        }

        // Fallback: parse the full text content and split by emoji patterns
        const mainEl = document.querySelector('main') || document.body;
        const fullText = mainEl.innerText;
        const fullHtml = mainEl.innerHTML;

        return {
            itemCount: items.length,
            selectorUsed: items.length > 0 ? 'dom' : 'text',
            fullText: fullText,
            fullHtml: fullHtml.substring(0, 500000),  // Limit size
            itemTexts: Array.from(items).slice(0, 5).map(el => ({
                tag: el.tagName,
                classes: el.className,
                text: el.innerText.substring(0, 200)
            }))
        };
    }""")
    return data


def save_page_html(page, output_path):
    """Save the full page HTML for debugging / offline parsing."""
    html_content = page.content()
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Saved full page HTML to {output_path}")


def parse_biases_from_html(html_path):
    """Parse the saved HTML to extract structured bias data using BeautifulSoup.
    This is more reliable than page.evaluate() for complex DOM structures.
    """
    from bs4 import BeautifulSoup
    from utils import clean_text

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    result = {
        'title': '',
        'description': '',
        'categories': [],
        'resources': [],
        'cheatSheet': None,
        'citation': None,
        'sourceUrl': TARGET_URL,
    }

    # Page title
    h1 = soup.find('h1')
    if h1:
        result['title'] = clean_text(h1.get_text())

    # Find all text blocks and structure them
    # We'll look for patterns: emoji + title, then following content blocks

    # First, let's understand the DOM structure by looking at key classes
    # growth.design is a Next.js app, so classes are often hashed

    # Strategy: find all headings and group content between them
    categories_data = {
        'Information': {'description': '', 'count': 29, 'biases': []},
        'Meaning': {'description': '', 'count': 31, 'biases': []},
        'Time': {'description': '', 'count': 24, 'biases': []},
        'Memory': {'description': '', 'count': 17, 'biases': []},
    }

    # Find category sections by looking for these keywords in headings
    all_headings = soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])

    # Try to find accordion/collapsible items
    # Common patterns in React/Next.js sites
    accordion_items = (
        soup.find_all(attrs={'data-state': True}) or
        soup.find_all(attrs={'data-radix-collection-item': True}) or
        soup.find_all(class_=lambda c: c and ('accordion' in c.lower() if isinstance(c, str) else any('accordion' in x.lower() for x in c))) or
        []
    )

    print(f"  Found {len(accordion_items)} accordion items")
    print(f"  Found {len(all_headings)} headings")

    # Parse the full text content to extract biases
    body = soup.find('body') or soup
    full_text = body.get_text(separator='\n')

    # Try to identify bias entries by emoji + title pattern
    # Cognitive biases on growth.design typically have emoji icons
    import re

    # Pattern: emoji followed by bias name
    emoji_pattern = re.compile(
        r'([\U0001F300-\U0001F9FF\U00002600-\U000027BF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF])\s*\n?\s*(.+?)(?:\n|$)'
    )

    # Find all links (for sources)
    all_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = clean_text(a.get_text())
        if href and not href.startswith('#') and not href.startswith('javascript:'):
            if href.startswith('/'):
                href = 'https://growth.design' + href
            all_links.append({'text': text, 'url': href})

    result['allLinks'] = all_links

    # Store raw text for further processing in convert_to_markdown.py
    result['rawText'] = full_text
    result['categories'] = [
        {'name': k, 'description': v['description'], 'expectedCount': v['count'], 'biases': v['biases']}
        for k, v in categories_data.items()
    ]

    return result


def main():
    print("=" * 60)
    print("Growth.design Psychology Scraper")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        # Launch with persistent context (inherits Chrome session)
        print("\nLaunching browser with Chrome profile...")
        try:
            context = launch_browser(pw)
        except Exception as e:
            print(f"ERROR launching with Chrome profile: {e}")
            print("Trying with fresh browser (you may need to log in)...")
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context()

        page = context.new_page()

        # Navigate to target
        print(f"\nNavigating to {TARGET_URL}...")
        for attempt in range(MAX_RETRIES):
            try:
                page.goto(TARGET_URL, wait_until="networkidle", timeout=PAGE_LOAD_TIMEOUT_MS)
                break
            except Exception as e:
                print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
                if attempt == MAX_RETRIES - 1:
                    print("FATAL: Could not load page")
                    context.close()
                    sys.exit(1)
                time.sleep(2 ** attempt)

        # Wait for page content to render
        print("Waiting for page to fully render...")
        page.wait_for_timeout(3000)

        # Check if we're authenticated (look for expand buttons)
        expand_count = page.locator('button:has-text("Expand")').count()
        if expand_count == 0:
            # Try alternative: look for any interactive elements
            alt_count = page.locator('[data-state="closed"]').count()
            if alt_count == 0:
                print("\nWARNING: No expandable sections found.")
                print("This might mean:")
                print("  - You're not logged in (check growth.design subscription)")
                print("  - The page structure has changed")
                print("  - The page hasn't fully loaded yet")
                print("\nProceeding anyway to capture what's visible...")
            else:
                print(f"Found {alt_count} collapsible sections (via data-state)")
        else:
            print(f"Found {expand_count} expandable sections")

        # Expand all sections
        print("\nExpanding all sections...")
        expanded = expand_all_sections(page)

        # Wait for expansions to settle
        page.wait_for_timeout(2000)

        # Save the full page HTML for reliable parsing
        html_path = OUTPUT_DIR / "growth_design_psychology_full.html"
        save_page_html(page, html_path)

        # Extract data via JS (first pass)
        print("\nExtracting data via JavaScript...")
        js_data = extract_data(page)

        # Extract detailed bias info (second pass)
        print("Extracting detailed bias information...")
        detail_data = extract_detailed_biases(page)

        # Close browser
        context.close()

    # Parse the saved HTML with BeautifulSoup (more reliable)
    print("\nParsing saved HTML with BeautifulSoup...")
    bs_data = parse_biases_from_html(html_path)

    # Merge data from both extraction methods
    final_data = {
        'title': bs_data.get('title') or js_data.get('title', ''),
        'description': bs_data.get('description') or js_data.get('description', ''),
        'sourceUrl': TARGET_URL,
        'extractedAt': js_data.get('extractedAt', ''),
        'categories': bs_data.get('categories', []),
        'allLinks': bs_data.get('allLinks', []),
        'resources': bs_data.get('resources', []),
        'cheatSheet': bs_data.get('cheatSheet'),
        'citation': bs_data.get('citation'),
        'rawText': bs_data.get('rawText', ''),
        'jsData': {
            'structuredData': js_data.get('structuredData'),
            'pageContent': {
                'text': js_data.get('pageContent', {}).get('text', '')[:50000],
                'allLinks': js_data.get('pageContent', {}).get('allLinks', []),
            }
        },
        'detailData': {
            'itemCount': detail_data.get('itemCount', 0),
            'selectorUsed': detail_data.get('selectorUsed', ''),
            'itemTexts': detail_data.get('itemTexts', []),
        },
        'sectionsExpanded': expanded,
    }

    # Save JSON
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"\nData saved to {DATA_FILE}")
    print(f"Full HTML saved to {html_path}")
    print(f"Sections expanded: {expanded}")
    print(f"Links found: {len(final_data['allLinks'])}")

    # Summary
    print("\n" + "=" * 60)
    print("SCRAPING COMPLETE")
    print(f"Next step: python convert_to_markdown.py")
    print("=" * 60)


if __name__ == '__main__':
    main()
