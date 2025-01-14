from flask import Flask, request, jsonify
import pandas as pd
from recommendation import recommend_articles

app = Flask(__name__)

# Load preprocessed data
df = pd.read_csv('news_articles.csv')

@app.route('/recommend', methods=['GET'])
def recommend():
    article_idx = int(request.args.get('article_idx', 0))
    num_recommendations = int(request.args.get('num', 5))
    recommendations = recommend_articles(article_idx, num_recommendations)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
