from netflix_recommender import get_recommendations

movie_title = input("🎬 Enter a movie title: ")
recommendations = get_recommendations(movie_title)

print(f"\n📽️ Recommendations for '{movie_title}':\n")
print(recommendations)
