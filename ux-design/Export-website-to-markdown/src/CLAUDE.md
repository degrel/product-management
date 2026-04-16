# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status: COMPLETE

Successfully created a local offline copy of "The Mystery School" course from `learn.makeartnotcontent.com` (Teachable platform).

## What Was Accomplished

1. **Scraped 132 lecture pages** using `scrape_course.py` with authenticated session cookies
2. **Cleaned 792 tracking elements** (Facebook, Heap, Sift analytics) from all HTML files
3. **Generated organized index** with proper course structure and navigation
4. **Converted internal links** to work locally between lecture pages

## Course Structure

The course contains **8 books** with **132 lectures** total:

| # | Book Title | Lectures |
|---|-----------|----------|
| 1 | THE BOOK OF GENESIS: How To Regain Your Artistic Brain | 2 |
| 2 | THE BOOK OF TRANSFORMATION: The Art Of Discipline | 24 |
| 3 | THE BOOK OF MENTAL HEALTH: The Cure For Overthinking | 12 |
| 4 | THE BOOK OF DARES: Run With The Wolves | 24 |
| 5 | THE BOOK OF PURPOSE: What's Your Message? | 19 |
| 6 | THE BOOK OF INFLUENCE: Make Art Not Content | 19 |
| 7 | THE BOOK OF MONEY: Business Art | 28 |
| 8 | THE BOOK OF APPENDIX: Resources To Help You Rise | 4 |

## Directory Structure

```
/
├── CLAUDE.md                 # This file
├── scrape_course.py          # Scraping script (requires cookies.json)
├── cleanup_course.py         # Cleanup and organize script
├── cookies.json              # Browser cookies (not committed)
├── ressources/               # Original browser-saved page (reference)
│   ├── The Mystery School.htm
│   └── The Mystery School_files/
└── course_offline/           # FINAL OUTPUT - offline course
    ├── index.html            # Main navigation (organized by book)
    ├── assets/
    │   ├── css/              # Downloaded stylesheets
    │   ├── images/           # Downloaded images
    │   └── js/               # JavaScript (minimal)
    └── lectures/
        └── {lecture_id}.html # 132 lecture pages
```

## Usage

Open the offline course in a browser:
```bash
open course_offline/index.html
```

Or serve locally:
```bash
cd course_offline && python3 -m http.server 8000
# Then open http://localhost:8000
```

## Content Types

Lectures are marked with icons in the index:
- 🎬 Video lectures (Wistia player - requires internet for video playback)
- 🎧 Audio content
- 📄 Text/articles

## Technical Notes

- **Source platform**: Teachable (teachablecdn.com)
- **Course ID**: 465756
- **Videos**: Use Wistia player, stream from internet (not downloaded)
- **Images**: Most downloaded locally to `assets/images/`
- **Navigation**: Sidebar links converted to local paths, "Back to course" links to `../index.html`

## Scripts

### scrape_course.py
Requires: `beautifulsoup4`, `requests`
```bash
# Export cookies from browser while logged in, save as cookies.json
python3 scrape_course.py
```

### cleanup_course.py
Requires: `beautifulsoup4`
```bash
python3 cleanup_course.py
```
- Removes tracking scripts (Facebook, Heap, Sift, Google Analytics)
- Extracts course structure from original HTML
- Regenerates index.html with proper book organization
