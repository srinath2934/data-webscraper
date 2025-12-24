"""
Parsing helpers for Futurepedia-like pages.

Contains small, testable functions that extract tool metadata from HTML.
"""
from __future__ import annotations

from typing import Dict, List
from bs4 import BeautifulSoup

BASE_URL = "https://www.futurepedia.io"


def parse_tool_cards_from_html(html: str) -> List[Dict]:
    """
    Parse HTML and return a list of tool dicts with keys:
    Name, Category, Description, Pricing, Link
    """
    soup = BeautifulSoup(html, "lxml")
    tools = []

    for card in soup.select("a"):
        name = card.get("data-tool-name") or card.get("aria-label") or None
        if not name:
            title_el = card.select_one(".tool-name, .title, h2, h3")
            if title_el:
                name = title_el.get_text(strip=True)
        if not name:
            continue
        name = name.strip()

        link = card.get("href", "").strip()
        if link:
            from urllib.parse import urljoin
            link = urljoin(BASE_URL, link)

        category = card.get("data-tool-category") or ""
        badge = card.find("span", class_="inline-flex")
        pricing = "Paid" if badge and "Paid" in badge.get_text() else "Free"

        desc_el = card.find("p", class_=lambda x: x and "text-gray-500" in x)
        description = desc_el.get_text(strip=True) if desc_el else ""

        tools.append({
            "Name": name,
            "Category": category,
            "Description": description,
            "Pricing": pricing,
            "Link": link,
        })

    return tools
