import Movie
import fresh_tomatoes


def main():
    # add movies' fields
    interstellar = Movie.Movie("Interstellar",
                               "http://www.hdwallpapers.in/download/"
                               "interstellar-3840x2160.jpg",
                               "https://www.youtube.com/watch?v=0vxOhd4qlnA")
    inception = Movie.Movie("Inception", "https://upload.wikimedia.org/"
                                         "wikipedia/en/1/18/Inception_OST.jpg",
                            "https://www.youtube.com/watch?v=8hP9D6kZseM")
    shutter_island = Movie.Movie("Shutter Island",
                                 "https://d.ibtimes.co.uk/en/full/1396267/"
                                 "shutter-island-movie-be-made-into-tv-series"
                                 ".jpg"
                                 "https://www.youtube.com/watch?v=5iaYLCiq5RM")
    enemy_at_the_gate = Movie.Movie("Enemy at the Gate",
                                    "http://www.miniih.com/miniiblog/mergen/"
                                    "files/Enemy%20At%20The%20Gates.jpg",
                                    "www.google.com")
    dark_night_rise = Movie.Movie("Dark Night Rise",
                                  "http://paulmmartinblog.files.wordpress.com/"
                                  "2011/07/the_dark_knight_poster.jpg",
                                  "https://www.youtube.com/"
                                  "watch?v=EXeTwQWrcwY")
    xmen = Movie.Movie("X-Men First Class",
                       "http://vignette2.wikia.nocookie.net/marvelmovies/"
                       "images/"
                       "6/64/Pakorn-x-men-first-class- "
                       "25197968-2560-1810.jpg/revision/"
                       "latest?cb=20120921143114",
                       "www.google.com")
    # Add movies to the list
    movies = [interstellar, inception, shutter_island, enemy_at_the_gate,
              dark_night_rise, xmen]
    # Load the main page
    fresh_tomatoes.open_movies_page(movies)
main()
