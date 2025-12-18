import requests
import random

API_KEY = "***"

def get_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}"
    response = requests.get(url).json()
    
    if "genres" in response:
        return {genre["name"].lower(): genre["id"] for genre in response["genres"]}
    else:
        print("Error fetching genres:", response)
        return {}

def get_movies_by_genre(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url).json()
    
    if "results" in response and response["results"]:
        return response["results"]
    else:
        print("No movies found for this genre!")
        return []

def recommend_movie():
    genres = get_genres()
    if not genres:
        return

    print("\nAvailable Genres:")
    for genre in genres.keys():
        print(f"- {genre.capitalize()}")

    user_choice = input("\nEnter a movie genre: ").strip().lower()

    if user_choice not in genres:
        print("Invalid genre! Please choose from the list.")
        return

    genre_id = genres[user_choice]
    movies = get_movies_by_genre(genre_id)

    if movies:
        selected_movie = random.choice(movies)
        print(" Recommended Movie:")
        print(f"Title: {selected_movie['title']}")
        print(f"Overview: {selected_movie['overview']}")
    else:
        print("No movies found in this genre. Try another one!")

recommend_movie()
