# BBC Scraper API

A small FastAPI service that takes the URL of a BBC News article and returns its title, subtitle, lead image and body text as JSON.

## How it works

- `Scrapper.py` fetches the page with `requests`, parses it with BeautifulSoup, and picks out the headline, bold subtitle, first image and article body.
- `main.py` exposes a single endpoint, `GET /json?url=<article url>`, that runs the scraper and returns the result.

## Run it

```bash
pip install fastapi uvicorn requests beautifulsoup4
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs, click **Try it out** on `/json`, paste a BBC News article URL and run the request.

Example:

```bash
curl "http://127.0.0.1:8000/json?url=https://www.bbc.com/news/world-12345678"
```

Response:

```json
[
  {
    "Title": "...",
    "Sub Title": "...",
    "Image": "https://...",
    "Body": "..."
  }
]
```

## Notes

- The scraper relies on BBC's CSS class names at the time it was written. If BBC changes its markup, update the selectors in `Scrapper.py`.
- For personal and educational use. Check the BBC terms of use before scraping at scale.
