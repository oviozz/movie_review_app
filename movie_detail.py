
from movie_api_call import MovieApi
from PyQt5.QtGui import QPixmap
from function_navigation import Navigation
import webbrowser


class MovieDetail(MovieApi):
    tralier_url = None
    def __init__(self, region):
        super().__init__(region)

    def movie_details(self, movie_name):
        movie_info = dict(self.movie.details(self.movie.search(movie_name)[0]['id']))

        return {
            'Title': movie_name,
            'ImageURL': f'{self.image_link}{movie_info["poster_path"]}',
            'Overview': movie_info['overview'],
            'Rating': f"Rating: {round(float(movie_info['vote_average']), 2)}",
            'Release': f"Release date: {movie_info['release_date']}",
            'Saftey': 'PG-13' if not movie_info['adult'] else 'Rated R',
            'Tralier': f'https://www.youtube.com/watch?v={movie_info["videos"]["results"][0]["key"]}' if
            movie_info['videos']['results'] else False,
            'Language': f"Language: {movie_info['spoken_languages'][0]['english_name']}",
            'Gernes': f"Genre: {', '.join(sorted([gerne['name'] for gerne in movie_info['genres']], key=lambda x: len(x))[:2])}"
        }

    def detail_apply(self, movie_name, title, img_url, overview, rating, release, saftey, language, gernes, screen):

        try:
            movie_detail_items = self.movie_details(movie_name)

            title.setText(movie_name)
            self.image_load(img_url, movie_detail_items)
            overview.setText(movie_detail_items['Overview'])
            rating.setText(movie_detail_items["Rating"])
            release.setText(movie_detail_items['Release'])
            saftey.setText(movie_detail_items['Saftey'])
            language.setText(movie_detail_items['Language'])
            gernes.setText(movie_detail_items['Gernes'])
            MovieDetail.tralier_url = movie_detail_items['Tralier']

            return Navigation.screen_navigator(screen, 1)

        except:
            print('Not working')

    def image_load(self, image, movie_detail_items):
        image_data = MovieDetail.req.get(movie_detail_items['ImageURL']).content

        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        image.setPixmap(pixmap)

    @classmethod
    def youtube_button(cls):
        if MovieDetail.tralier_url:
            return webbrowser.open(MovieDetail.tralier_url)




