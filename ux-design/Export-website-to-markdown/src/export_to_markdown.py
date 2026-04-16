#!/usr/bin/env python3
"""
Export all Mystery School lectures to a single optimized markdown file.
Extracts only the essential content, removing all HTML boilerplate.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import html

BASE_DIR = Path(__file__).parent
RESSOURCES_HTML = BASE_DIR / "ressources" / "The Mystery School.htm"
LECTURES_DIR = BASE_DIR / "course_offline" / "lectures"
OUTPUT_FILE = BASE_DIR / "course_offline" / "The_Mystery_School_Complete.md"


def extract_course_structure(html_path):
    """Extract sections and lectures from the original HTML sidebar."""
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    sections = []

    for section_div in soup.find_all('div', class_='course-section'):
        title_div = section_div.find('div', class_='section-title')
        if not title_div:
            continue

        section_name = title_div.get_text(strip=True)
        section_name = re.sub(r'\s+', ' ', section_name).strip()

        lectures = []
        for li in section_div.find_all('li', {'data-lecture-id': True}):
            lecture_id = li.get('data-lecture-id')
            name_span = li.find('span', class_='lecture-name')
            if name_span:
                lecture_name = name_span.get_text(strip=True)
                lecture_name = re.sub(r'\s*\(\d+:\d+\)\s*', '', lecture_name).strip()
            else:
                lecture_name = f"Lecture {lecture_id}"

            lectures.append({'id': lecture_id, 'name': lecture_name})

        if lectures:
            sections.append({'name': section_name, 'lectures': lectures})

    return sections


def clean_text(text):
    """Clean and normalize text content."""
    # Decode HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    # Remove leading/trailing whitespace per line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_lecture_content(lecture_path):
    """Extract main content from a lecture HTML file."""
    if not lecture_path.exists():
        return None

    with open(lecture_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Remove scripts, styles, nav elements
    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'iframe']):
        tag.decompose()

    # Remove sidebar navigation
    for sidebar in soup.find_all(class_=re.compile(r'sidebar|nav|menu')):
        sidebar.decompose()

    # Remove hidden elements
    for hidden in soup.find_all(style=re.compile(r'display:\s*none')):
        hidden.decompose()

    # Try to find main content area
    main_content = None

    # Look for lecture content specifically
    content_selectors = [
        ('div', {'class': 'lecture-content'}),
        ('div', {'class': 'lecture-text-container'}),
        ('div', {'class': 'fr-view'}),  # Froala editor content
        ('div', {'class': 'attachment-wistia-player'}),  # Video description
        ('main', {}),
        ('article', {}),
    ]

    for tag, attrs in content_selectors:
        main_content = soup.find(tag, attrs)
        if main_content:
            break

    # If no specific content area found, try to get body content
    if not main_content:
        main_content = soup.find('body')

    if not main_content:
        return None

    # Convert to markdown-friendly text
    result_parts = []

    # Process paragraphs
    for p in main_content.find_all(['p', 'div'], recursive=True):
        # Skip if it's a container with children that are also being processed
        if p.find(['p', 'div']):
            continue
        text = p.get_text(strip=True)
        if text and len(text) > 10:  # Skip very short fragments
            result_parts.append(text)

    # Process lists
    for ul in main_content.find_all(['ul', 'ol']):
        for li in ul.find_all('li', recursive=False):
            text = li.get_text(strip=True)
            if text:
                result_parts.append(f"- {text}")

    # Process headings
    for h in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text = h.get_text(strip=True)
        if text:
            level = int(h.name[1])
            result_parts.append(f"\n{'#' * (level + 1)} {text}\n")

    # If we didn't get much, try getting all text
    if len(result_parts) < 3:
        all_text = main_content.get_text(separator='\n')
        return clean_text(all_text)

    return clean_text('\n\n'.join(result_parts))


def main():
    print("=" * 60)
    print("Exporting Mystery School to Markdown")
    print("=" * 60)

    # Get course structure
    print("\nExtracting course structure...")
    sections = extract_course_structure(RESSOURCES_HTML)
    total_lectures = sum(len(s['lectures']) for s in sections)
    print(f"Found {len(sections)} sections with {total_lectures} lectures")

    # Build markdown content
    md_parts = []

    # Title
    md_parts.append("# The Mystery School")
    md_parts.append("*Make Art Not Content - Complete Course*\n")
    md_parts.append("---\n")

    # Table of contents
    md_parts.append("## Table of Contents\n")
    for i, section in enumerate(sections, 1):
        section_anchor = section['name'].lower().replace(' ', '-').replace(':', '')
        md_parts.append(f"{i}. [{section['name']}](#{section_anchor})")
    md_parts.append("\n---\n")

    # Process each section
    processed = 0
    skipped = 0

    for section_idx, section in enumerate(sections, 1):
        print(f"\n[{section_idx}/{len(sections)}] {section['name']}")

        md_parts.append(f"\n## {section['name']}\n")

        for lecture in section['lectures']:
            lecture_id = lecture['id']
            lecture_name = lecture['name']
            lecture_path = LECTURES_DIR / f"{lecture_id}.html"

            content = extract_lecture_content(lecture_path)

            md_parts.append(f"\n### {lecture_name}\n")

            if content and len(content) > 50:
                md_parts.append(content)
                processed += 1
                print(f"  ✓ {lecture_name[:50]}...")
            else:
                md_parts.append("*[Video/Audio content - view in browser]*\n")
                skipped += 1

        md_parts.append("\n---\n")

    # Write output
    output_content = '\n'.join(md_parts)

    # Final cleanup
    output_content = re.sub(r'\n{4,}', '\n\n\n', output_content)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output_content)

    # Stats
    file_size = OUTPUT_FILE.stat().st_size
    print("\n" + "=" * 60)
    print("EXPORT COMPLETE!")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Size: {file_size / 1024:.1f} KB")
    print(f"Lectures with content: {processed}")
    print(f"Video/audio only: {skipped}")
    print("=" * 60)


if __name__ == '__main__':
    main()
