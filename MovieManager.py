import json

from Movie import Movie

class MovieManager:
    def __init__(self, json_file='C:/Users/CEGET/OneDrive/Desktop/PythonWork/Project0/MovieList.json'):
        self.movies = []
        self.json_file = json_file
        self.load_json(self.json_file)

    def add_movie(self, movie):
        self.movies.append(movie)

    #This function compares the title of the current movie 
    # (converted to lowercase) with the input title (also converted to lowercase). 
    #ensures that the comparison is case-insensitive
    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def remove_movie(self, title):
        movie = self.find_movie(title)
        if movie:
            self.movies.remove(movie)

    #==============================================================================================
    def list_movies(self):
        print("Listing all movie titles:\n")
        if not self.movies:
            print("No movies found in self.movies.")
        else:
            for movie in self.movies:
                    print(movie.title)

            """ else:
                print(f"Unexpected object found: {movie}") """

    """ def sort_movies(self, key):
        #sort movies based on the specified attribute.
        #the lambda function extrats the attribute value for sorting.
        self.movies.sort(key=lambda x: getattr(x, key))

    def filter_movies(self, key, value):
        return [movie for movie in self.movies if getattr(movie, key).lower() == value.lower()] """
    
    #==============================================================================================
    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([movie.__dict__ for movie in self.movies], file)

    def load_json(self, filename):
        try:
            with open(filename, 'r') as file:
                movies_data = json.load(file)
                for movie_data in movies_data:
                    movie = Movie(**movie_data)
                    self.add_movie(movie)
        #Handle exception
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading JSON file: {e}")
    