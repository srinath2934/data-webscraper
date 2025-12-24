# futurepedia-ai-tools-scraper

This project is a custom Python-based web scraper built using requests and BeautifulSoup. It extracts data from the Futurepedia website, the largest AI tools directory. The script collects information about AI tools (name, description, categories, tags, links, and other metadata) and saves the results to a JSON file for further analysis.

## Features

- Lightweight scraper using requests + BeautifulSoup
- Extracts tool metadata (name, description, categories, tags, links)
- Outputs results as JSON for easy consumption
- Configurable output directory and simple logging

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt` (if present)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/srinath2934/data-webscraper.git
cd data-webscraper
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main scraper script (replace `scraper.py` with the actual entrypoint if different):

```bash
python scraper.py
```

Scraped results are saved to the `outputs/` directory by default (if implemented). Check the script's CLI options or config to change output path and logging level.

## Project structure

A quick overview of the repository layout and what each item is for:

````
data-webscraper/
├─ README.md                 # Project README (this file)
├─ requirements.txt          # Python dependencies
├─ scraper.py                # Main scraping script
├─ utils/
│  ├─ parser.py              # HTML parsing helpers
│  └─ downloader.py          # Request / download helpers
├─ outputs/
│  ├─ tools.json             # Example saved JSON output of scraped tools
│  └─ logs/                  # Log files from scraping runs
├─ tests/                    # Unit tests
└─ docs/                     # Additional documentation
````

Notes:
- `scraper.py` is the entry point. Run it with:

  ```bash
  python scraper.py
  ```

- Dependencies are listed in `requirements.txt`. Install with:

  ```bash
  pip install -r requirements.txt
  ```

- Scraped results are saved in `outputs/` by default. You can change the output path via CLI args or config (if implemented).
- Add or edit files in `utils/` for parsing, downloading, or data cleaning logic.

## Contributing

Contributions, issues and feature requests are welcome. Feel free to check the issues page or open a pull request.

## License

If you have a license, add it here (e.g., MIT). If not, consider adding one to clarify usage terms.
