from MovieManager import MovieManager
from Movie import Movie

def Main():
    manager = MovieManager()
    #load movies from JSON file at the start
    manager.load_json('MovieList.json')

    while True:
        print("1. Add Movie")
        print("2. Search Movie")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. List All Movies")
        print("6. Mark as Watched/Unwatched")
        print("7. Generate Reports")
        print("8. Save to File")
        print("9. Load from File")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            director = input("Director: ")
            genre = input("Genre: ")
            year = int(input("Year: "))
            rating = float(input("Rating: "))
            duration = int(input("Duration: "))
            description = input("Description: ")
            movie = Movie(title, director, genre, year, rating, duration, description)
            manager.add_movie(movie)
        
            #create a Movie object
            new_movie = Movie(title, director, genre, year, rating, duration, description)
            manager.add_movie(new_movie)

        elif choice == '2':
            #search movie
            title = input("Enter movie title to search: ")
            movie = manager.find_movie(title)
            if movie:
                print(movie)
            else:
                print("Movie not found.")

        elif choice == '3':
            #code to update movie information
            pass

        elif choice == '4':
            title = input("Enter movie title to delete: ")
            manager.remove_movie(title)

        elif choice == '5':
            manager.list_movies()

        elif choice == '6':
            #code to mark as watched/unwatched
            pass

        elif choice == '7':
            #code to generate reports
            #
            pass

        elif choice == '8':
            filename = input("Enter filename to save: ")
            if filename.endswith('.json'):
                manager.save_json(filename)
            else:
                print("Invalid file format. Please use .json.")

        elif choice == '9':
            filename = input("Enter filename to load: ")
            if filename.endswith('.json'):
                manager.load_json(filename)
            else:
                print("Invalid file format. Please use .json.")

        elif choice == '10':
            break

        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    Main()   
