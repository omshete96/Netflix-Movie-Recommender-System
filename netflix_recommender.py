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

# Function to get recommendations based on the theme
def get_recommendations_by_theme(theme, cosine_sim=cosine_sim):
    theme = theme.lower()
    
    # Filter movies that match the theme
    filtered_movies = df[df['listed_in'].str.lower().str.contains(theme, na=False)]
    
    if filtered_movies.empty:
        return "❌ No movies found for the given theme."
    
    # Combine relevant content for similarity calculation
    tfidf_matrix_theme = tfidf.transform(filtered_movies['content'])
    
    # Calculate cosine similarity for the filtered movies
    cosine_sim_theme = cosine_similarity(tfidf_matrix_theme, tfidf_matrix_theme)
    
    # We are comparing within the filtered set, so indices will be local to the filtered set
    sim_scores = list(enumerate(cosine_sim_theme.mean(axis=1)))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Pick top 5 movies or fewer if not enough movies
    sim_scores = sim_scores[1:6]  # Top 5
    
    movie_indices = [i[0] for i in sim_scores]
    
    # Return movie titles, handle cases where fewer than 5 results are available
    return filtered_movies['title'].iloc[movie_indices].tolist()

