import requests
from bs4 import BeautifulSoup


class Scraper(object):

    __nat_dex = []
    __generation = 0
    __min = 0
    __max = 0
    __my_formatter = ''
    __my_printer = ''

    def __init__(self, the_formatter, the_printer):
        self.__my_formatter = the_formatter
        self.__my_printer = the_printer

    def gen_decider(self):
        pass

    def set_nat_dex(self, the_dex):
        pass

    def get_nat_dex(self):
        pass

    def set_generation(self, the_gen):
        pass

    def get_generation(self):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass

    def web_scraper(self):
        dex_data = []
        url = 'http://pokemondb.net/pokedex/national'
        r = requests.get(url).text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = table.find_all('span')

        for card in cards:
            stuffs = card.find_all(['a', 'small'])
            dex_data.append([stuff.text for stuff in stuffs[1:4]])

        dex_data1 = self.__my_formatter.hash_stripper(dex_data)
        dex_data2 = self.__my_formatter.type_formatter(dex_data1)
        out = self.__my_formatter.formatter(dex_data2, self.__min, self.__max)
        return out

    def print(self, the_gen, the_list):
        self.__my_printer.printer(the_gen, the_list)