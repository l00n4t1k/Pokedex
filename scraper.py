import requests
from formatter import Formatter as f
from bs4 import BeautifulSoup


class Scraper(object):

    __nat_dex = []
    __generation = 0
    __min = 0
    __max = 0
    __my_formatter = ''

    def __init__(self, the_formatter):
        self.__my_formatter = the_formatter

    def printer(self):
        print()
        print('-----------------------------------------')
        print()
        print('Gen ', self.get_generation(), ' List')
        print('----------')
        for datum in self.__nat_dex:
            print(datum)

    def gen_decider(self):
        gen = self.get_generation()
        if gen == 1:
            self.__min = 0
            self.__max = 151
        elif gen == 2:
            self.__min = 151
            self.__max = 251
        elif gen == 3:
            self.__min = 251
            self.__max = 386
        elif gen == 4:
            self.__min = 386
            self.__max = 493
        elif gen == 5:
            self.__min = 493
            self.__max = 649
        elif gen == 6:
            self.__min = 649
            self.__max = 721

    def set_nat_dex(self, the_dex):
        self.__nat_dex = the_dex

    def get_nat_dex(self):
        return self.__nat_dex

    def set_generation(self, the_gen):
        self.__generation = the_gen

    def get_generation(self):
        return self.__generation

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

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

        dex_data1 = f.hash_stripper(dex_data)
        dex_data2 = f.type_formatter(dex_data1)
        out = f.formatter(dex_data2, self.__min, self.__max)
        return out

