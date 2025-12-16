import requests

API_KEY = "2c217e9a9bb8450d925e740c9e614d39"

def fetch_news():
    articles = []
    
    queries = [
        "lithium mining",
        "critical minerals",
        "cobalt mining",
        "rare earth minerals",
        "nickel mining",
        "copper mining",
        "graphite mining"
    ]
    
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

if __name__ == "__main__":
    news = fetch_news()
    print("Found " + str(len(news)) + " articles")
    for item in news[:5]:
        print("- " + item["headline"])
