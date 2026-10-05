import requests
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  
from config import NOVA_DIR
from Body.Listen.ListenJs import Listen
from Body.Speak.Speak import Speak

try:
    with open(os.path.join(NOVA_DIR, "DataBase", "news"), encoding="utf-8") as key_file:
        KEY = key_file.read().strip()
except OSError:
    KEY = ""
    print("News API data unavailable; news commands are disabled.")

def clean_news_headlines(headlines):
    cleaned_headlines = []
    for headline in headlines:
        # Add your cleaning logic here
        cleaned_headlines.append(headline)
    return cleaned_headlines

def latestnews(main_url):
    main_page = requests.get(main_url).json()
    articles = main_page["articles"][:5]
    news_items = [f"Today's {ordinal(i+1)} news: {article['title']}\n" for i, article in enumerate(articles)]
    news_items = clean_news_headlines(news_items)
    return ''.join(news_items)

def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


def get_news_by_category(category):
    api_dict = {
        "business": [
            {"name": "Business Insider", "url": f"https://newsapi.org/v2/top-headlines?sources=business-insider&apiKey={KEY}"},
            {"name": "CNBC", "url": f"https://newsapi.org/v2/top-headlines?sources=cnbc&apiKey={KEY}"}
        ],
        "technology": [
            {"name": "TechCrunch", "url": f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={KEY}"}
        ],
        "sports": [
            {"name": "ESPN", "url": f"https://newsapi.org/v2/top-headlines?sources=espn&apiKey={KEY}"}
        ],
        "health": [
            {"name": "Medical News Today", "url": f"https://newsapi.org/v2/top-headlines?sources=medical-news-today&apiKey={KEY}"}
        ],
        "science": [
            {"name": "National Geographic", "url": f"https://newsapi.org/v2/top-headlines?sources=national-geographic&apiKey={KEY}"}
        ],
        "entertainment": [
            {"name": "BuzzFeed", "url": f"https://newsapi.org/v2/top-headlines?sources=buzzfeed&apiKey={KEY}"}
        ]

    }

    category_urls = api_dict.get(category.lower())
    if category_urls:
        for source in category_urls:
            news = latestnews(source["url"])
            Speak(f"From {source['name']}: {news}")
    else:
        print("Invalid category")

def get_user_preference():
    Speak("Which field news do you want to listen, [business], [technology], [sports], [health], [science], [entertainment]")
    field = Listen()
    if field.lower() == '':
        for category in ["business", "technology", "sports", "health", "science", "entertainment"]:
            get_news_by_category(category)
    else:
        get_news_by_category(field)

# get_user_preference()
