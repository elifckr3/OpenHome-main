import requests

def suggest_movies(api_key):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        print("DEBUGG!!!!!!")
        movies = response.json().get('results', [])[:5]  # Get top 5 movies
        movie_titles = [movie['title'] for movie in movies]
        return "Popular movies right now: " + ", ".join(movie_titles)
    else:
        return "I couldn't fetch movie suggestions at the moment."
        print("DIDT WORK!!")
