#!/usr/bin/env python3
"""
Cleanup and organize the scraped Mystery School course.
- Removes tracking scripts from all lecture pages
- Extracts course structure from original HTML
- Regenerates index.html with proper sections and order
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Paths
BASE_DIR = Path(__file__).parent
RESSOURCES_HTML = BASE_DIR / "ressources" / "The Mystery School.htm"
COURSE_DIR = BASE_DIR / "course_offline"
LECTURES_DIR = COURSE_DIR / "lectures"

# Tracking scripts/patterns to remove
TRACKING_PATTERNS = [
    r'heap\.load\([^)]+\)',
    r'window\.heap\s*=',
    r'fbq\s*\(',
    r'_sift\.push',
    r'heapShouldTrackUser',
    r'cdn\.heapanalytics\.com',
    r'cdn\.sift\.com',
    r'www\.facebook\.com/tr',
    r'google-analytics\.com',
    r'googletagmanager\.com',
]

def extract_course_structure(html_path):
    """Extract sections and lectures from the original HTML sidebar."""
    print(f"Reading course structure from {html_path}...")

    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    sections = []

    # Find all course sections
    for section_div in soup.find_all('div', class_='course-section'):
        # Get section title
        title_div = section_div.find('div', class_='section-title')
        if not title_div:
            continue

        # Extract section name (remove SVG and extra whitespace)
        section_name = title_div.get_text(strip=True)
        # Clean up the section name
        section_name = re.sub(r'\s+', ' ', section_name).strip()

        lectures = []

        # Find all lectures in this section
        for li in section_div.find_all('li', {'data-lecture-id': True}):
            lecture_id = li.get('data-lecture-id')

            # Get lecture name
            name_span = li.find('span', class_='lecture-name')
            if name_span:
                lecture_name = name_span.get_text(strip=True)
                # Clean up (remove duration if present)
                lecture_name = re.sub(r'\s*\(\d+:\d+\)\s*', '', lecture_name).strip()
            else:
                lecture_name = f"Lecture {lecture_id}"

            # Get lecture type from icon
            icon_use = li.find('use')
            lecture_type = 'text'
            if icon_use:
                href = icon_use.get('xlink:href', '')
                if 'Video' in href:
                    lecture_type = 'video'
                elif 'VolumeUp' in href:
                    lecture_type = 'audio'
                elif 'Subject' in href:
                    lecture_type = 'text'

            lectures.append({
                'id': lecture_id,
                'name': lecture_name,
                'type': lecture_type
            })

        if lectures:
            sections.append({
                'name': section_name,
                'lectures': lectures
            })

    print(f"Found {len(sections)} sections with {sum(len(s['lectures']) for s in sections)} lectures")
    return sections


def clean_html_file(filepath):
    """Remove tracking scripts and clean up an HTML file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    removed_count = 0

    # Remove tracking scripts by src pattern
    tracking_domains = [
        'heapanalytics.com',
        'sift.com',
        'facebook.com',
        'fbevents',
        'google-analytics.com',
        'googletagmanager.com',
        'facebook.net',
        'doubleclick.net',
    ]

    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.string or ''

        # Check if it's a tracking script
        should_remove = False

        for domain in tracking_domains:
            if domain in src:
                should_remove = True
                break

        # Check script content for tracking patterns
        if not should_remove and text:
            for pattern in TRACKING_PATTERNS:
                if re.search(pattern, text):
                    should_remove = True
                    break

        if should_remove:
            script.decompose()
            removed_count += 1

    # Remove tracking pixels (1x1 images)
    for img in soup.find_all('img'):
        src = img.get('src', '')
        width = img.get('width', '')
        height = img.get('height', '')

        if ('facebook.com/tr' in src or
            (width == '1' and height == '1') or
            'pixel' in src.lower()):
            img.decompose()
            removed_count += 1

    # Remove noscript tracking elements
    for noscript in soup.find_all('noscript'):
        text = str(noscript)
        if 'facebook.com/tr' in text or 'pixel' in text.lower():
            noscript.decompose()
            removed_count += 1

    # Remove empty script tags
    for script in soup.find_all('script'):
        if not script.get('src') and not (script.string or '').strip():
            script.decompose()

    # Write cleaned content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    return removed_count


def generate_index_html(sections, output_path):
    """Generate a nicely organized index.html with sections."""

    # Type icons
    type_icons = {
        'video': '🎬',
        'audio': '🎧',
        'text': '📄'
    }

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Mystery School - Offline Course</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #141414;
            color: #f0f0f0;
            line-height: 1.6;
        }
        h1 {
            color: #fff;
            border-bottom: 2px solid #333;
            padding-bottom: 15px;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #888;
            margin-bottom: 30px;
        }
        .section {
            margin-bottom: 40px;
            background: #1e1e1e;
            border-radius: 10px;
            padding: 20px;
        }
        .section-title {
            color: #fff;
            font-size: 1.2em;
            font-weight: 600;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #333;
        }
        .lecture-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .lecture-item {
            margin: 0;
        }
        .lecture-link {
            color: #a0c4ff;
            text-decoration: none;
            display: flex;
            align-items: center;
            padding: 12px 15px;
            background: #252525;
            border-radius: 6px;
            margin-bottom: 8px;
            transition: all 0.2s ease;
        }
        .lecture-link:hover {
            background: #333;
            transform: translateX(5px);
        }
        .lecture-icon {
            margin-right: 12px;
            font-size: 1.1em;
        }
        .lecture-name {
            flex: 1;
        }
        .stats {
            color: #666;
            font-size: 0.9em;
            margin-top: 30px;
            text-align: center;
        }
        .missing {
            opacity: 0.5;
            pointer-events: none;
        }
        .missing::after {
            content: " (not downloaded)";
            color: #ff6b6b;
            font-size: 0.8em;
        }
    </style>
</head>
<body>
    <h1>The Mystery School</h1>
    <p class="subtitle">Make Art Not Content - Offline Course Copy</p>
"""

    total_lectures = 0
    available_lectures = 0

    for section in sections:
        html += f'    <div class="section">\n'
        html += f'        <div class="section-title">{section["name"]}</div>\n'
        html += f'        <ul class="lecture-list">\n'

        for lecture in section['lectures']:
            lecture_id = lecture['id']
            lecture_name = lecture['name']
            lecture_type = lecture['type']
            icon = type_icons.get(lecture_type, '📄')

            # Check if lecture file exists
            lecture_file = LECTURES_DIR / f"{lecture_id}.html"
            exists = lecture_file.exists()

            total_lectures += 1
            if exists:
                available_lectures += 1

            css_class = "lecture-link" if exists else "lecture-link missing"

            html += f'            <li class="lecture-item">\n'
            html += f'                <a href="lectures/{lecture_id}.html" class="{css_class}">\n'
            html += f'                    <span class="lecture-icon">{icon}</span>\n'
            html += f'                    <span class="lecture-name">{lecture_name}</span>\n'
            html += f'                </a>\n'
            html += f'            </li>\n'

        html += f'        </ul>\n'
        html += f'    </div>\n\n'

    html += f'    <p class="stats">{available_lectures} of {total_lectures} lectures available offline</p>\n'
    html += """</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated index.html with {len(sections)} sections")
    print(f"Available: {available_lectures}/{total_lectures} lectures")


def main():
    print("=" * 60)
    print("Mystery School Course Cleanup")
    print("=" * 60)

    # Step 1: Extract course structure
    print("\n[1/3] Extracting course structure...")
    sections = extract_course_structure(RESSOURCES_HTML)

    # Step 2: Clean all lecture HTML files
    print("\n[2/3] Cleaning tracking scripts from lectures...")
    lecture_files = list(LECTURES_DIR.glob("*.html"))
    total_removed = 0

    for i, filepath in enumerate(lecture_files, 1):
        removed = clean_html_file(filepath)
        total_removed += removed
        if removed > 0:
            print(f"  [{i}/{len(lecture_files)}] {filepath.name}: removed {removed} tracking elements")

    print(f"  Total tracking elements removed: {total_removed}")

    # Step 3: Generate new index
    print("\n[3/3] Generating organized index.html...")
    generate_index_html(sections, COURSE_DIR / "index.html")

    print("\n" + "=" * 60)
    print("CLEANUP COMPLETE!")
    print(f"Open: {COURSE_DIR / 'index.html'}")
    print("=" * 60)


if __name__ == '__main__':
    main()
