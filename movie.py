class Movie:
    def __init__(self, title, director, genre, year, rating, duration, description):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.rating = rating
        self.duration = duration
        self.description = description
        self.watched = False

    def mark_watched(self):
        self.watched = True

    def mark_unwatched(self):
        self.watched = False

    def __str__(self):
        return f"{self.title} ({self.year}), Directed by {self.director}, Rating: {self.rating}"
