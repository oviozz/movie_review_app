
from movie_api_call import MovieApi
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from threading import *


class SearchListLoad(MovieApi):
    def __init__(self, name, region):
        super().__init__(region)
        self.movie_list = self.movie_popular_detail(self.movie.search(name))

    def thread(self, *args):
        movie_load = Thread(target=self.movie_list_load, args=args)
        movie_load.start()

    def movie_list_load(self, lists):
        for title, image_url in self.movie_list.items():
            if not ('w500None' in image_url):
                image_data = MovieApi.req.get(image_url).content

                item = QListWidgetItem(title)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                icon = QIcon(pixmap)
                item.setIcon(icon)
                lists.addItem(item)
