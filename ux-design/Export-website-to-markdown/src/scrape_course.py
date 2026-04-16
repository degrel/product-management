#!/usr/bin/env python3
"""
Mystery School Course Scraper
Scrapes the Teachable course and creates a local offline copy.

USAGE:
1. Log into learn.makeartnotcontent.com in your browser
2. Export your cookies using a browser extension (e.g., "EditThisCookie" or "Cookie-Editor")
   - Export as JSON and save to 'cookies.json' in this directory
3. Run: python3 scrape_course.py

Alternatively, you can pass cookies via command line:
   python3 scrape_course.py --cookie "_teachable_session=YOUR_SESSION_COOKIE"
"""

import os
import re
import json
import time
import argparse
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup
import requests

# Configuration
BASE_URL = "https://learn.makeartnotcontent.com"
COURSE_ID = "465756"
OUTPUT_DIR = Path("course_offline")
ASSETS_DIR = OUTPUT_DIR / "assets"
LECTURES_DIR = OUTPUT_DIR / "lectures"

# Lecture IDs extracted from the saved HTML (134 lectures total)
LECTURE_IDS = [
    "8598951", "8734815", "8886468", "8886877", "8986816", "9019960", "9022531",
    "9033828", "9061808", "9106068", "9123891", "9304811", "9483186", "9669878",
    "9828514", "9954378", "10356269", "11233631", "11362971", "11743885", "11756714",
    "11925540", "12084289", "12114744", "12114808", "12229202", "12287274", "12458583",
    "12754553", "14159433", "14159583", "14159984", "14160014", "14160123", "14160161",
    "14160278", "14160282", "14160287", "14606196", "15232016", "15675152", "15744029",
    "15897829", "16636509", "17070063", "17120429", "17348559", "17758538", "20478410",
    "21444354", "21445027", "21813183", "21830997", "22464200", "22465060", "22465568",
    "22776827", "22983261", "23009474", "23473198", "23551748", "23551753", "23560268",
    "23573896", "23575213", "23575529", "23650999", "23737415", "23737529", "23737589",
    "23841832", "23846521", "23909722", "24395511", "24579982", "24764091", "25102006",
    "25135654", "25245041", "27097470", "27097903", "27099578", "27099970", "27125984",
    "27160804", "27161738", "27216554", "27576694", "27587749", "27871545", "27885125",
    "29475297", "30093395", "30094455", "30275043", "30417622", "30854335", "30899936",
    "31212744", "31981630", "31981735", "31997861", "32033853", "32221423", "32221439",
    "32265875", "32591705", "32712997", "34246945", "35199489", "35843860", "36457991",
    "36894226", "38190972", "38282847", "39428003", "39896160", "41878133", "46231249",
    "46367180", "46904991", "47243449", "47601636", "49639533", "52289382", "58196471",
    "58948901", "59474001", "60134613", "62198905", "62283991", "62938177"
]

class CourseScraper:
    def __init__(self, cookies=None, cookie_string=None):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })

        if cookies:
            for cookie in cookies:
                self.session.cookies.set(
                    cookie.get('name', cookie.get('Name')),
                    cookie.get('value', cookie.get('Value')),
                    domain=cookie.get('domain', cookie.get('Domain', '.makeartnotcontent.com'))
                )
        elif cookie_string:
            # Parse cookie string like "name=value; name2=value2"
            for part in cookie_string.split(';'):
                if '=' in part:
                    name, value = part.strip().split('=', 1)
                    self.session.cookies.set(name.strip(), value.strip())

        self.downloaded_assets = {}

    def setup_directories(self):
        """Create output directory structure."""
        OUTPUT_DIR.mkdir(exist_ok=True)
        ASSETS_DIR.mkdir(exist_ok=True)
        (ASSETS_DIR / "images").mkdir(exist_ok=True)
        (ASSETS_DIR / "css").mkdir(exist_ok=True)
        (ASSETS_DIR / "js").mkdir(exist_ok=True)
        LECTURES_DIR.mkdir(exist_ok=True)

    def download_page(self, url):
        """Download a page and return its HTML content."""
        try:
            print(f"  Downloading: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"  Error downloading {url}: {e}")
            return None

    def download_asset(self, url, asset_type="images"):
        """Download an asset (image, CSS, JS) and return local path."""
        if url in self.downloaded_assets:
            return self.downloaded_assets[url]

        if not url.startswith(('http://', 'https://')):
            if url.startswith('//'):
                url = 'https:' + url
            elif url.startswith('/'):
                url = BASE_URL + url
            else:
                return url  # Relative path, keep as-is

        try:
            # Generate local filename
            parsed = urllib.parse.urlparse(url)
            filename = os.path.basename(parsed.path)
            if not filename:
                filename = "index"

            # Add hash to avoid conflicts
            url_hash = str(hash(url))[-8:]
            name, ext = os.path.splitext(filename)
            if not ext:
                ext = ".bin"
            filename = f"{name}_{url_hash}{ext}"

            local_path = ASSETS_DIR / asset_type / filename
            relative_path = f"assets/{asset_type}/{filename}"

            # Download file
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            with open(local_path, 'wb') as f:
                f.write(response.content)

            self.downloaded_assets[url] = relative_path
            print(f"    Downloaded asset: {filename}")
            return relative_path

        except Exception as e:
            print(f"    Failed to download asset {url}: {e}")
            return url

    def process_html(self, html, lecture_id):
        """Process HTML content - download assets and rewrite URLs."""
        soup = BeautifulSoup(html, 'html.parser')

        # Download and rewrite images
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                new_src = self.download_asset(src, "images")
                img['src'] = f"../{new_src}"

        # Download and rewrite CSS
        for link in soup.find_all('link', rel='stylesheet'):
            href = link.get('href')
            if href and not href.startswith('data:'):
                new_href = self.download_asset(href, "css")
                link['href'] = f"../{new_href}"

        # Rewrite internal navigation links to local paths
        for a in soup.find_all('a'):
            href = a.get('href', '')
            # Match lecture URLs
            match = re.search(r'/courses/(?:enroll/)?lectures/(\d+)', href)
            if match:
                lid = match.group(1)
                a['href'] = f"{lid}.html"
            # Match course curriculum URL
            elif f'/courses/enrolled/{COURSE_ID}' in href or f'/courses/{COURSE_ID}' in href:
                a['href'] = "../index.html"

        # Remove tracking scripts and unnecessary JS
        for script in soup.find_all('script'):
            src = script.get('src', '')
            # Keep only essential scripts, remove analytics/tracking
            if any(x in src for x in ['analytics', 'facebook', 'fbevents', 'heap', 'recaptcha', 'google']):
                script.decompose()

        # Remove iframes (often ads or tracking)
        for iframe in soup.find_all('iframe'):
            iframe.decompose()

        return str(soup)

    def extract_lecture_info(self, html):
        """Extract lecture title and content from HTML."""
        soup = BeautifulSoup(html, 'html.parser')

        # Try to find lecture title
        title_elem = soup.find('h2', class_='lecture-title') or soup.find('title')
        title = title_elem.get_text(strip=True) if title_elem else "Untitled"

        # Find main content area
        content_elem = soup.find('div', class_='lecture-content') or soup.find('main')

        return title, content_elem

    def scrape_lecture(self, lecture_id):
        """Scrape a single lecture page."""
        url = f"{BASE_URL}/courses/{COURSE_ID}/lectures/{lecture_id}"
        html = self.download_page(url)

        if not html:
            return None

        # Check if we're actually logged in (look for login prompt)
        if 'Sign In' in html and 'password' in html.lower():
            print("  ERROR: Not logged in! Please check your cookies.")
            return None

        processed_html = self.process_html(html, lecture_id)
        return processed_html

    def create_index_page(self, lectures_info):
        """Create an index page with links to all lectures."""
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Mystery School - Offline Course</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #1a1a1a;
            color: #fff;
        }
        h1 { color: #fff; border-bottom: 2px solid #333; padding-bottom: 10px; }
        h2 { color: #ccc; margin-top: 30px; }
        ul { list-style: none; padding: 0; }
        li { margin: 8px 0; }
        a {
            color: #6ab0f3;
            text-decoration: none;
            display: block;
            padding: 10px;
            background: #2a2a2a;
            border-radius: 5px;
            transition: background 0.2s;
        }
        a:hover { background: #3a3a3a; }
        .section { margin-bottom: 30px; }
        .completed { color: #4caf50; }
    </style>
</head>
<body>
    <h1>The Mystery School</h1>
    <p>Offline course copy - Make Art Not Content</p>
    <ul>
"""
        for lecture_id, title in lectures_info.items():
            html += f'        <li><a href="lectures/{lecture_id}.html">{title}</a></li>\n'

        html += """    </ul>
</body>
</html>
"""
        return html

    def run(self):
        """Main scraping process."""
        print("=" * 60)
        print("Mystery School Course Scraper")
        print("=" * 60)

        self.setup_directories()

        # Test authentication
        print("\nTesting authentication...")
        test_url = f"{BASE_URL}/courses/enrolled/{COURSE_ID}"
        test_html = self.download_page(test_url)

        if not test_html or ('Sign In' in test_html and 'password' in test_html.lower()):
            print("\nERROR: Authentication failed!")
            print("Please ensure you have valid cookies in cookies.json")
            print("or pass cookies via --cookie argument")
            return False

        print("Authentication OK!\n")

        lectures_info = {}

        # Scrape all lectures
        print(f"Scraping {len(LECTURE_IDS)} lectures...")
        for i, lecture_id in enumerate(LECTURE_IDS, 1):
            print(f"\n[{i}/{len(LECTURE_IDS)}] Lecture {lecture_id}")

            html = self.scrape_lecture(lecture_id)
            if html:
                # Save processed HTML
                output_path = LECTURES_DIR / f"{lecture_id}.html"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(html)

                # Extract title for index
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.find('title')
                lectures_info[lecture_id] = title.get_text(strip=True) if title else f"Lecture {lecture_id}"

            # Rate limiting
            time.sleep(1)

        # Create index page
        print("\nCreating index page...")
        index_html = self.create_index_page(lectures_info)
        with open(OUTPUT_DIR / "index.html", 'w', encoding='utf-8') as f:
            f.write(index_html)

        print("\n" + "=" * 60)
        print("COMPLETE!")
        print(f"Output directory: {OUTPUT_DIR.absolute()}")
        print(f"To view: open {OUTPUT_DIR}/index.html in your browser")
        print("=" * 60)

        return True


def load_cookies(cookies_file):
    """Load cookies from JSON file."""
    with open(cookies_file, 'r') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description='Scrape Mystery School course')
    parser.add_argument('--cookies', default='cookies.json', help='Path to cookies JSON file')
    parser.add_argument('--cookie', help='Cookie string (e.g., "_teachable_session=xxx")')
    args = parser.parse_args()

    cookies = None
    cookie_string = None

    if args.cookie:
        cookie_string = args.cookie
    elif os.path.exists(args.cookies):
        print(f"Loading cookies from {args.cookies}")
        cookies = load_cookies(args.cookies)
    else:
        print(f"ERROR: No cookies found!")
        print(f"Please create {args.cookies} or use --cookie argument")
        print("\nTo export cookies:")
        print("1. Install 'Cookie-Editor' browser extension")
        print("2. Log into learn.makeartnotcontent.com")
        print("3. Click Cookie-Editor icon -> Export -> JSON")
        print("4. Save as 'cookies.json' in this directory")
        return

    scraper = CourseScraper(cookies=cookies, cookie_string=cookie_string)
    scraper.run()


if __name__ == '__main__':
    main()
