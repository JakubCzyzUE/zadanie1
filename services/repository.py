from services.utils import read_file
from models.movies import Movie
from models.links import Links
from models.ratings import Ratings

#czyta dane z pliku i konwertuje je do listy
def get_movies_data():
    data = read_file('data/movies.csv')
    movies = []
    for movie in data.split('\n'):
        if len(movie) and 'movieId' not in movie:
            movie = movie.split(',')
            movies.append(movie)

    return movies
def get_csv_data(CsvName):
    data = read_file(CsvName)
    tab = []
    for x in data.split('\n'):
        if len(x) and 'movieId' not in x:
            x = x.split(',')
            tab.append(x)

    return tab

#zwraca zserializowane (za pomocą metody magicznej __dict__) listę obiektów Movie
def get_movies():
    print(get_movies_data())
    return [Movie(movie[0], movie[1], movie[2]).__dict__ for movie in get_movies_data()]

def get_links():
    print(get_csv_data('data/links.csv'))
    return [Links(tab[0], tab[1], tab[2]).__dict__ for tab in get_csv_data('data/links.csv')]

def get_ratings():
    print(get_csv_data('data/ratings.csv'))
    return [Ratings(tab[0], tab[1], tab[2], tab[3]).__dict__ for tab in get_csv_data('data/ratings.csv')]
def get_tags():
    print(get_csv_data('data/tags.csv'))
    return [Links(tab[0], tab[1], tab[2]).__dict__ for tab in get_csv_data('data/tags.csv')]