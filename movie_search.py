
from movie_api_call import MovieApi
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap, QIcon

class MovieSearch(MovieApi):
    def __init__(self, name, region):
        super().__init__(region)
        self.name = name

    def movie_popular_detail(self):
        self.recommendations = self.movie.search(self.name)

        return {recommendation.title: f'{self.image_link}{recommendation.poster_path}' for recommendation in
                self.recommendations}


class SearchListLoad(MovieSearch):
    def __init__(self, name, region):
        super().__init__(name, region)
        self.movie_list = self.movie_popular_detail()

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