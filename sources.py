sources.py
# Critical Minerals News Sources
# These are RSS feeds and websites we'll scrape for news

SOURCES = {
    "reuters_mining": {
        "name": "Reuters Mining",
        "url": "https://www.reuters.com/markets/commodities/",
        "type": "website"
    },
    "mining_dot_com": {
        "name": "Mining.com",
        "url": "https://www.mining.com/feed/",
        "type": "rss"
    },
    "sp_global": {
        "name": "S&P Global Commodities",
        "url": "https://www.spglobal.com/commodityinsights/en/rss-feed/metals",
        "type": "rss"
    }
}

# Keywords we care about
MINERALS = [
    "lithium",
    "cobalt", 
    "nickel",
    "graphite",
    "rare earth",
    "copper",
    "manganese"
]