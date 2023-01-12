
from tmdbv3api import Discover
from movie_api_call import MovieApi
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from function_navigation import Navigation
from threading import *


class MovieGerne(MovieApi):
    def __init__(self, region):
        super().__init__(region)

    def gernes_id(self, gerne):
        self.gernes = {
                'Action': 28,
                'Adventure': 12,
                'Animation': 16,
                'Comedy': 35,
                'Drama': 18,
                'Family': 10751,
                'Horror': 27,
                'Mystery': 9648,
                'Romance': 10749,
                'Science fiction': 878,
                }

        return self.gernes[gerne.capitalize()]


    def movies_gerne(self, name):

        self.discover = Discover()

        self.movie = self.discover.discover_movies({
            'with_genres': self.gernes_id(name),
            'sort_by': 'popularity.desc',
            #'page': 2
        })

        return {recommendation.title: f'{self.image_link}{recommendation.poster_path}' for recommendation in
                self.movie}


class GerneListLoad(MovieGerne):
    def __init__(self, gerne, region):
        super().__init__(region)
        self.movie_list = self.movies_gerne(gerne)

    def thread(self, lists, screen):
        movie_load = Thread(target=self.movie_list_load, args=(lists, ))
        movie_load.start()

        Navigation.screen_navigator(screen, 0)

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

