import requests
import pandas as pd

API_KEY = 'your_newsapi_key'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

def fetch_articles(category, country='us'):
    params = {
        'apiKey': API_KEY,
        'category': category,
        'country': country,
        'pageSize': 20
    }
    response = requests.get(BASE_URL, params=params)
    articles = response.json().get('articles', [])
    return [
        {
            'title': article['title'],
            'description': article['description'],
            'content': article['content'],
            'url': article['url'],
            'category': category
        }
        for article in articles
    ]

categories = ['technology', 'sports', 'business', 'politics']
data = []
for category in categories:
    data.extend(fetch_articles(category))

df = pd.DataFrame(data)
df.to_csv('news_articles.csv', index=False)
print("Data saved to 'news_articles.csv'")

