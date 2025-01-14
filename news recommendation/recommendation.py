from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


# Load the data
df = pd.read_csv('news_articles.csv')

# Combine relevant text fields for better feature extraction
df['text'] = df['title'] + " " + df['description']

# Vectorize the text data
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['text'].fillna(''))

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend articles based on a given article index
def recommend_articles(article_idx, num_recommendations=5):
    sim_scores = list(enumerate(cosine_sim[article_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_articles = sim_scores[1:num_recommendations+1]
    recommendations = [df.iloc[i[0]]['title'] for i in top_articles]
    return recommendations

# Example usage
print("Recommendations for Article 0:")
print(recommend_articles(0))
