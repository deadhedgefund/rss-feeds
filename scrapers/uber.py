import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.uber.com/en-US/blog/engineering/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    articles = []
    seen = set()
    
    # Ищем все ссылки на статьи блога
    for a in soup.find_all("a", href=True):
        href = a["href"]
        
        # Фильтруем именно ссылки на посты блога
        if "/blog/" in href:
            if href.endswith("/blog/engineering/") or href.endswith("/blog/"):
                continue
                
            full_url = href if href.startswith("http") else f"https://www.uber.com{href}"
            
            if full_url in seen:
                continue

            # Пробуем достать заголовок
            title = ""
            heading = a.find(["h2", "h3", "h4", "h5", "p"])
            if heading:
                title = heading.get_text(strip=True)
            if not title:
                title = a.get_text(strip=True)

            # Пропускаем технические ссылки вроде "Read more", "Engineering", пустые
            if not title or len(title) < 15 or title.lower() in ["read more", "engineering", "read article"]:
                continue

            seen.add(full_url)
            articles.append({
                "title": title,
                "url": full_url,
                "description": f'Read article: <a href="{full_url}">{title}</a>'
            })

    print(f"[Uber Scraper] Found {len(articles)} articles.")
    return articles[:20]
