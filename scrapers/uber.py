import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.uber.com/en-US/blog/engineering/"
    base_url = "https://www.uber.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    articles = []
    seen = set()
    
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/blog/" in href and href not in ["/blog/engineering/", "/en-US/blog/engineering/"]:
            full_url = href if href.startswith("http") else base_url + href
            if full_url in seen:
                continue
            seen.add(full_url)
            
            title = a.get_text(strip=True)
            if not title or len(title) < 15 or "Read more" in title:
                header = a.find(["h2", "h3", "h4"])
                title = header.get_text(strip=True) if header else None
                
            if title and len(title) >= 15:
                articles.append({
                    "title": title,
                    "url": full_url,
                    "description": f'Read full story on <a href="{full_url}">Uber Engineering</a>'
                })
    return articles[:15]
