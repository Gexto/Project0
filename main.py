from movie import movie 
from MovieManager import MovieManager

def main():
     manager = MovieManager()

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
    
if __name__ == "__main__":
    main()   
