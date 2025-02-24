#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import argparse
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Text cleaning function
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    return text

# Text preprocessing using spaCy (lemmatization, stopword removal)
def preprocess_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

def load_dataset(filepath, sample_size=200):
    df = pd.read_excel(filepath)
    df = df[['title', 'overview']].dropna()  # Keep only relevant columns and drop NaN values
    df['overview'] = df['overview'].apply(clean_text)  # Basic cleaning
    df['overview'] = df['overview'].apply(preprocess_text)  # Apply spaCy preprocessing
    df = df.sample(n=min(sample_size, len(df)), random_state=42)
    return df


# Compute TF-IDF similarity
def compute_similarity(data, query, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')  
    tfidf_matrix = vectorizer.fit_transform(data['overview'])  # Convert overviews to TF-IDF vectors

    query_vector = vectorizer.transform([query])  # Convert query to TF-IDF vector
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()  # Compute similarity scores

    data = data.copy()  # Make a copy to avoid modifying the original dataframe
    data['similarity_score'] = similarity_scores  # Add similarity scores to the dataframe

    top_indices = similarity_scores.argsort()[-top_n:][::-1]  # Get indices of top_n highest scores
    
    recommendations = data.iloc[top_indices]  # Select top recommendations
    return recommendations[['title', 'overview', 'similarity_score']]  # Keep only relevant columns

if __name__ == "__main__":
    # Argument parser to allow command-line input
    parser = argparse.ArgumentParser(description="Movie Recommendation System")
    parser.add_argument("--file", type=str, default="tmdb_5000_movies.xlsx", help="Path to the dataset file")
    parser.add_argument("--query", type=str, required=True, help="User input describing preferred movie")
    parser.add_argument("--top_n", type=int, default=5, help="Number of recommendations to return")
    args = parser.parse_args()

    # Load dataset and compute recommendations
    dataset = load_dataset(args.file)
    results = compute_similarity(dataset, args.query, args.top_n)

    # Print recommendations
    print("\nTop Movie Recommendations (Ranked by Similarity Score):")
    for rank, row in enumerate(results.itertuples(), start=1):
        print(f"{rank}. {row.title} (Score: {row.similarity_score:.4f})")
        print(f"   Overview: {row.overview}\n")


# In[ ]:




