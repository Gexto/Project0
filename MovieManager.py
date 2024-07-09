import csv
import json

class MovieManager:
    def __init__(self):
        self.movies = []

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
    
    def list_movies(self):
        for movie in self.movies:
            print(movie)

    def sort_movies(self, key):
        #sort movies based on the specified attribute.
        #the lambda function extracts the attribute value for sorting.
        self.movies.sort(key=lambda x: getattr(x, key))

    def filter_movies(self, key, value):
        return [movie for movie in self.movies if getattr(movie, key).lower() == value.lower()]

    