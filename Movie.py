import webbrowser


# Database of movies
class Movie:
    """ Contains information about movies """
    def __init__(self, title, image_link, trailer_link):
        self.title = title
        self.poster_image_url = image_link
        self.trailer_youtube_url = trailer_link

    # Open web browser to show trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_link)