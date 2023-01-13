
from movie_api_call import MovieApi
from PyQt5.QtWidgets import QListWidgetItem
from function_navigation import Navigation
from PyQt5.QtGui import QPixmap, QIcon
from threading import *


class SearchListLoad(MovieApi):
    def __init__(self, name, region):
        super().__init__(region)
        self.movie_list = self.movie_popular_detail(self.movie.search(name))

    def thread(self, lists, screens):
        movie_load = Thread(target=self.movie_list_load, args=(lists,).start()
        
        Navigation.screen_navigator(screens, 2)

    def movie_list_load(self, lists, screens):
        for title, image_url in self.movie_list.items():
            if not ('w500None' in image_url):
                image_data = MovieApi.req.get(image_url).content

                item = QListWidgetItem(title)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                icon = QIcon(pixmap)
                item.setIcon(icon)
                lists.addItem(item)
