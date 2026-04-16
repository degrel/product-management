#!/usr/bin/env python3
"""Configuration for growth.design/psychology scraper."""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
DATA_FILE = OUTPUT_DIR / "growth_design_psychology_data.json"
MARKDOWN_FILE = OUTPUT_DIR / "growth_design_psychology.md"
SOURCES_DIR = OUTPUT_DIR / "sources"
SOURCES_INDEX_FILE = OUTPUT_DIR / "sources_index.md"

# URLs
TARGET_URL = "https://growth.design/psychology"

# Chrome profile for persistent auth (macOS default)
CHROME_USER_DATA_DIR = Path.home() / "Library" / "Application Support" / "Google" / "Chrome"
CHROME_PROFILE = "Default"

# Scraping delays
CLICK_DELAY_MS = 500
EXPAND_TIMEOUT_MS = 3000
PAGE_LOAD_TIMEOUT_MS = 30000
MAX_RETRIES = 3

# Source fetching
SOURCE_FETCH_DELAY = 1.5  # seconds between requests
SOURCE_FETCH_TIMEOUT = 15  # seconds per request
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
