#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset(filepath, sample_size=500):
    df = pd.read_excel(filepath)
    df = df[['title', 'overview']].dropna()  # Keep only relevant columns and drop NaN values
    df = df.sample(n=sample_size, random_state=42)  # Randomly select 200 rows
    return df

# Compute TF-IDF similarity
def compute_similarity(data, query, top_n=5):
    """
    Computes similarity between the user query and movie overviews using TF-IDF and cosine similarity.

    Args:
        data (pd.DataFrame): Movie dataset containing 'overview'.
        query (str): User query describing preferred movie type.
        top_n (int): Number of top recommendations to return.

    Returns:
        pd.DataFrame: Dataframe with top recommended movies and their similarity scores.
    """
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




