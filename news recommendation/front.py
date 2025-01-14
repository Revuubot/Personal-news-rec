import streamlit as st
import pandas as pd
import requests

BASE_URL = 'http://127.0.0.1:5000/recommend'

st.title("Personalized News Recommender")

# Load article data
df = pd.read_csv('news_articles.csv')

# User selects an article
article_idx = st.selectbox("Select an article to get recommendations:", range(len(df)))

if st.button("Get Recommendations"):
    response = requests.get(BASE_URL, params={'article_idx': article_idx, 'num': 5})
    recommendations = response.json()['recommendations']
    st.write("Recommended Articles:")
    for rec in recommendations:
        st.write(f"- {rec}")
