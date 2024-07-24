class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self._is_rented = False

    def rent(self):
        if not self._is_rented:
            self._is_rented = True
        return
    
    def return_movie(self):
        if self._is_rented:
            self._is_rented = False
        return
    
class MovieLibrary:
    def __init__(self):
        self._movie_collection = []

    def add_movie(self, movie):
        self._movie_collection.append(movie)

    def list_all_movies(self):
        for movie in self._movie_collection: 
                print(f"{movie.title} directed by {movie.director}")
                
    def list_available_movies(self):
        for movie in self._movie_collection:
            if movie._is_rented == False:
                print(f"{movie.title} directed by {movie.director}")
    
    def rent_movie(self, movie_title):
        for movie in self._movie_collection:
            if movie.title == movie_title and not movie._is_rented:
                print(f"Movie '{movie_title}' rented out.")
                movie.rent()
                return
            elif movie.title == movie_title and movie._is_rented:
                print(f"Movie '{movie_title}' is already rented out.")
                return
        print(f"Movie '{movie_title}' not found in the library.")
        return
                
    def return_movie(self, movie_title):
        for movie in self._movie_collection:
            if movie_title == movie.title and movie._is_rented:
                print(f"Movie '{movie_title}' returned")
                movie.return_movie()
                return
            elif movie_title == movie.title and not movie._is_rented:
                print(f"Movie '{movie_title}' was not rented out")
                return
        print(f"Movie '{movie_title}' not found in the library.")
        return