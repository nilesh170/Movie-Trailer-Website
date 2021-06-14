class Video():
    """This class stores the duration of movies title etc"""
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube, ratings, duration):
        # filling parent class with content
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = ratings
        self.duration = duration


class Movie(Video):
    """This class provides a way to store the information related to movies"""
    # Movie(Video):- Movie is the child class & Video is parent class
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube, release_date, director,
                 cast, budget, collection, ratings, duration):
        # sending content to the parent class Video
        Video.__init__(self, title, storyline, poster_image,
                       trailer_youtube, ratings, duration)
        self.release_date = release_date
        self.director = director
        self.cast = cast
        self.budget = budget
        self.collection = collection

    def show_info(self):
        # this function prints the data of the movies which is available
        print("-"*80)
        print("The Movie's name is = "+self.title)
        print("-"*80)
        print("The Movie's storyline is = "+self.storyline)
        print("-"*80)
        print("The Movie's release date is = "+self.release_date)
        print("-"*80)
        print("The Movie's director is = "+self.director)
        print("-"*80)
        print("The Movie's cast list contains : \n"+self.cast)
        print("-"*80)
        print("The Movie's budget is = "+self.budget)
        print("-"*80)
        print("The Movie's collection is = "+self.collection)
        print("-"*80)
        print("The Movie's ratings are = "+self.ratings)
        print("-"*80)
        print("The Movie's duration is "+self.duration)
        print("-"*80)


class TvShow(Video):
    # TvShow(Video):- Movie is the TvShow class & Video is parent class
    """This class provides a way to see the info about the tv shows"""
    def __init__(self, title, storyline, poster_image,
                 trailer_youtube, release_date, writer,
                 cast, seasons, network, ratings, duration):
        # sending content to the parent class Video
        Video.__init__(self, title, storyline, poster_image,
                       trailer_youtube, ratings, duration)
        self.release_date = release_date
        self.writer = writer
        self.cast = cast
        self.seasons = seasons
        self.network = network

    def show_info(self):
        # THis function prints the data of TvShows which is available
        print("-"*80)
        print("The show's name is = "+self.title)
        print("-"*80)
        print("The show's storyline is = "+self.storyline)
        print("-"*80)
        print("The show's release_date is "+self.release_date)
        print("-"*80)
        print("The show's writers are\n"+self.writer)
        print("-"*80)
        print("The show's cast list contains :\n"+self.cast)
        print("-"*80)
        print("The show's has "+self.seasons+" Seasons")
        print("-"*80)
        print("The show's network is "+self.network)
        print("-"*80)
        print("The show's ratings are "+self.ratings)
        print("-"*80)
        print("The show's duration is "+self.duration)
        print("-"*80)
