"""
HTTP helpers: create session and fetch with retries.

This module is intentionally small; the main session and retry logic is used by scraper.py.
"""
from __future__ import annotations

import logging
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

LOG = logging.getLogger(__name__)


def create_session(user_agent: str = "data-webscraper/1.0", timeout: int = 10) -> requests.Session:
    """Create and configure a requests.Session with retry strategy."""
    session = requests.Session()
    session.headers.update({"User-Agent": user_agent, "Accept": "text/html,application/xhtml+xml"})
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=(429, 500, 502, 503, 504))
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.timeout = timeout
    return session


def fetch(session: requests.Session, url: str, timeout: Optional[int] = None) -> Optional[str]:
    """Fetch a URL and return text or None. Logs on failure."""
    try:
        resp = session.get(url, timeout=timeout or getattr(session, "timeout", 10))
        resp.raise_for_status()
        return resp.text
    except Exception as exc:
        LOG.warning("Error fetching %s: %s", url, exc)
        return None
