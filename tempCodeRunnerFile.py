from netflix_recommender import get_recommendations_by_theme

theme = input("🎬 Enter a theme (e.g., Action, Drama, Sci-Fi, Comedy, Thriller): ")
recommendations = get_recommendations_by_theme(theme)

print(f"\n📽️ Recommendations for '{theme}':\n")

# Print each recommended movie on a new line
if isinstance(recommendations, list):
    for movie in recommendations:
        print(movie)
else:
    print(recommendations)
