#!/usr/bin/env python3
"""Shared utilities for growth.design/psychology export."""

import re
import hashlib
import html


def clean_text(text):
    """Clean and normalize text content.
    Adapted from export_to_markdown.py.
    """
    text = html.unescape(text)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def slugify(text):
    """Convert text to a URL-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def hash_url(url):
    """Return a short hash of a URL for unique filenames."""
    return hashlib.md5(url.encode()).hexdigest()[:8]
