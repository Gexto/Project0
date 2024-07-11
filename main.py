from MovieManager import MovieManager
from Movie import Movie

def Main():
    manager = MovieManager()
   
    while True:
        print("1. Add Movie")
        print("2. Search Movie")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. List All Movies")
        #print("6. Mark as Watched/Unwatched")
        #print("7. Generate Reports")
        print("8. Save to File")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            director = input("Director: ")
            genre = input("Genre: ")
            year = int(input("Year: "))
            rating = float(input("Rating: "))
            duration = int(input("Duration: "))
            description = input("Description: ")
            
        #=================================================================================================
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
        
        #Delete movie
        elif choice == '4':
            title = input("Enter movie title to delete: ")
            manager.remove_movie(title)

        #List movies
        elif choice == '5':
             manager.list_movies()
             
             """elif choice == '6':
            #code to mark as watched/unwatched
            pass 

            elif choice == '7':
                #code to generate reports
                #
                pass 
            """  
        elif choice == '8':
            filename = input("Enter filename to save: ")
            if filename.endswith('.json'):
                manager.save_json(filename)
            else:
                print("Invalid file format. Please use .json.")

        elif choice == '9':
            break

        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    Main()   

#manager.load_json('C:/Users/CEGET/OneDrive/Desktop/PythonWork/Project0/MovieList.json')