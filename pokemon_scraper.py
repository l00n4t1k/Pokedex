from scraper import Scraper


class PokemonScraper(Scraper):

    __my_controller = ''
    __my_formatter = ''
    __max = 0
    __min = 0

    def __init__(self, the_formatter, the_controller):
        self.__my_formatter = the_formatter
        self.__my_controller = the_controller
