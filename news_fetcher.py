import requests
import feedparser

API_KEY = "2c217e9a9bb8450d925e740c9e614d39"

# RSS feeds as backup (no limits)
RSS_FEEDS = [
    ("https://rss.nytimes.com/services/xml/rss/nyt/Business.xml", "NY Times"),
    ("https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml", "NY Times Climate"),
    ("https://feeds.bbci.co.uk/news/business/rss.xml", "BBC Business"),
    ("https://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "BBC Science"),
]

RSS_KEYWORDS = ["lithium", "cobalt", "nickel", "copper", "rare earth", "graphite", "mining", "battery", "ev", "electric vehicle", "mineral", "energy"]

def fetch_from_newsapi():
    articles = []
    queries = ["lithium mining", "critical minerals", "cobalt mining", "rare earth minerals", "nickel mining", "copper mining"]
    
    for query in queries:
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=5&apiKey={API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("status") == "ok":
                for article in data.get("articles", []):
                    articles.append({
                        "headline": article.get("title", "No title"),
                        "source": article.get("source", {}).get("name", "Unknown"),
                        "date": article.get("publishedAt", "No date")[:10],
                        "link": article.get("url", "#"),
                        "mineral": query.split()[0].title()
                    })
        except:
            pass
    return articles

def fetch_from_rss():
    articles = []
    for feed_url, source_name in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:30]:
                title = entry.get("title", "").lower()
                summary = entry.get("summary", "").lower()
                for keyword in RSS_KEYWORDS:
                    if keyword in title or keyword in summary:
                        articles.append({
                            "headline": entry.get("title", "No title"),
                            "source": source_name,
                            "date": entry.get("published", "No date")[:16],
                            "link": entry.get("link", "#"),
                            "mineral": keyword.title()
                        })
                        break
        except:
            pass
    return articles

def fetch_news():
    # Try NewsAPI first
    articles = fetch_from_newsapi()
    
    # If no results, use RSS backup
    if len(articles) == 0:
        articles = fetch_from_rss()
    
    return articles

if __name__ == "__main__":
    news = fetch_news()
    print("Found " + str(len(news)) + " articles")
    for item in news[:5]:
        print("- " + item["headline"])
