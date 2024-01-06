# recommendation_engine.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from app.models import listing

def generate_recommendations():
    # Fetch all products from the database
    lisitng = listing.objects.all()

    # Create a DataFrame with product data
    lisitng_data = pd.DataFrame(list(lisitng.values()))

    # Use TF-IDF vectorizer to convert the text data into numerical data
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(lisitng_data['name'])

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Generate recommendations based on similarity scores
    lisiting_indices = pd.Series(lisitng_data.index, index=lisitng_data['name'])
    recommendations = {}

    for idx, row in lisitng_data.iterrows():
        similar_products = list(enumerate(cosine_sim[idx]))
        similar_products = sorted(similar_products, key=lambda x: x[1], reverse=True)
        similar_products = similar_products[1:4]  # Exclude the product itself

        product_name = row['name']
        recommendations[product_name] = [lisitng_data['name'][i[0]] for i in similar_products]

    return recommendations
