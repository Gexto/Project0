class movie:
    def __init__(self, title, director, genre, year, rating, duration, description):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.rating = rating
        self.duration = duration
        self.description = description
        self.watched = False