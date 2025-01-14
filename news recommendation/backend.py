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

@app.route("/form")
def login():
    return"<html><head><title>Register</title></head><body><h1>Register</h1><form method="post" action="/register"><input type="text" name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required> <button type="submit">Register</button></form></body></html>"




