class Movie(object):
    """Movie class

    Args:
        trailer_youtube_url(str): Defaults to ''
        title(str): Defaults to ''
        poster_image_url(str): Defaults to ''

    """
    def __init__(self, trailer_youtube_url='', title = '', poster_image_url =''):
        super(Movie, self).__init__()
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
