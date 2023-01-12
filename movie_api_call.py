
from tmdbv3api import TMDb, Movie
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from threading import *
import requests


class MovieApi:
    req = requests.Session()

    def __init__(self, region):
        self.tmdb = TMDb()
        self.tmdb.language = region

        self.tmdb.api_key = '0b243a8843cc55c9e1ba6cdeae3cf6fb'
        self.image_link = 'https://image.tmdb.org/t/p/w500'
        self.movie = Movie()

    def movie_popular_detail(self, popular):

        return {recommendation.title: f'{self.image_link}{recommendation.poster_path}' for recommendation in
                popular}

class MovieListLoad(MovieApi):
    def __init__(self, region):
        super().__init__(region)
        self.movie_list = self.movie_popular_detail(self.movie.popular())

    def movie_list_load(self, lists):
        for title, image_url in self.movie_list.items():
            image_data = MovieApi.req.get(image_url).content

            # Create a QListWidgetItem with the title and image
            item = QListWidgetItem(title)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            icon = QIcon(pixmap)
            item.setIcon(icon)
            lists.addItem(item)

    def language_change(self, lists):
        load = Thread(target=self.movie_list_load, args=(lists,)).start()
