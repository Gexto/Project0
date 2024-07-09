import csv
import json

class MovieManager:
    def __init__(self):
        self.movies = []
        
    def add_movie(self, movie):
        self.movies.append(movie)

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def remove_movie(self, title):
        movie = self.find_movie(title)
        if movie:
            self.movies.remove(movie)