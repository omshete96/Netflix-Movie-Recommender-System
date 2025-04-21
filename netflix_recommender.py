import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('custom_netflix.csv')

# Fill any NaNs
df.fillna('', inplace=True)

# Combine relevant content into one feature for analysis
df['content'] = df['description'] + ' ' + df['listed_in'] + ' ' + df['director'] + ' ' + df['cast']

# Vectorize content using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['content'])

# Cosine similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map titles to index
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()

# Function to recommend movies
def get_recommendations(title, cosine_sim=cosine_sim):
    title = title.lower()
    idx = indices.get(title)
    if idx is None:
        return "❌ Title not found in dataset."
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5

    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]
