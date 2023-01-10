
import sys

class Navigation:
    index = 0
    @staticmethod
    def screen_navigator(switch, screen):
        return switch.setCurrentIndex(screen)


    @staticmethod
    def exit():
        sys.exit()

    @classmethod
    def current_index(cls, screen):
        Navigation.index = screen

    @staticmethod
    def return_index():
        return Navigation.index


class Region:

    @staticmethod
    def region_code(region):
        region_code = {
            'USA':'en',
            'China':'zh',
            'Hindi': 'hi',
            'Korean': 'ko',
            'Japanese': 'ja',
            'France': 'fr',
        }

        return region_code[region]