import os
import re
from datetime import datetime, timezone
from feedgen.feed import FeedGenerator

from scrapers import uber

FEEDS_CONFIG = [
    {
        "id": "uber",
        "title": "Uber Engineering Blog",
        "link": "https://www.uber.com/blog/engineering/",
        "desc": "Unofficial RSS feed for Uber Engineering",
        "scraper": uber.scrape,
        "filename": "feeds/uber.xml"
    },
]

def sanitize_xml(text):
    """Удаляет недопустимые для XML управляющие символы."""
    if not text:
        return ""
    # Разрешены только символы: 0x9, 0xA, 0xD и диапазон от 0x20 до 0xD7FF
    return re.sub(r'[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD]', '', str(text))

def generate_feed(config):
    print(f"--> Scraping {config['title']}...")
    try:
        articles = config["scraper"]()
    except Exception as e:
        print(f"Error scraping {config['title']}: {e}")
        articles = []

    fg = FeedGenerator()
    fg.id(config["link"])
    fg.title(sanitize_xml(config["title"]))
    fg.link(href=config["link"], rel="alternate")
    fg.description(sanitize_xml(config["desc"]))
    fg.language("en")

    for art in articles:
        fe = fg.add_entry()
        fe.id(art["url"])
        fe.title(sanitize_xml(art["title"]))
        fe.link(href=art["url"])
        fe.description(sanitize_xml(art.get("description", "")))
        fe.pubDate(datetime.now(timezone.utc))

    os.makedirs(os.path.dirname(config["filename"]), exist_ok=True)
    fg.rss_file(config["filename"], pretty=True)
    print(f"--> Successfully saved: {config['filename']} (articles: {len(articles)})")

def main():
    for config in FEEDS_CONFIG:
        generate_feed(config)

if __name__ == "__main__":
    main()
