import media
import movie_data
from fresh_tomatoes import open_movies_page

print 'entertainment starting'

# Init empty list to store movies. Used by fresh_tomatoes.
movies = []

for item in movie_data.data:
    # ** should split up the dict automatically. - stackoverflow
    movie = media.Movie(**item)
    movies.append(movie)

# Call fresh_tomatoes with our movies list.
open_movies_page(movies)

print "entertainment complete"
