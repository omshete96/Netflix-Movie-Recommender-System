# 🎬 Netflix Movie Recommender System

A terminal-based movie recommendation system that suggests similar movies based on descriptions, genres, directors, and cast. It uses TF-IDF vectorization and cosine similarity to find and recommend top related movies.

---

## 🚀 Features

- 📚 Content-based filtering
- 🧠 TF-IDF Vectorizer from `scikit-learn`
- 🔍 Cosine Similarity for matching
- 🎥 Uses custom dataset with titles, descriptions, genres, cast & directors
- 🖥️ Terminal input/output (no web interface)

---

## 🗂️ Dataset Fields (`custom_netflix.csv`)

- `title` – Movie title  
- `description` – Short movie summary  
- `listed_in` – Genre(s)  
- `director` – Director name  
- `cast` – Leading cast members  
