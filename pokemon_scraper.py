from scraper import Scraper
from bs4 import BeautifulSoup
import requests


class PokemonScraper(Scraper):

    __my_controller = ''
    __my_formatter = ''
    __max = 0
    __min = 0
    __nat_dex = []
    __local_dex = []
    __generation = 0
    __my_printer = ''

    def __init__(self, the_formatter, the_printer):
        self.__my_formatter = the_formatter
        self.__my_printer = the_printer

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
        elif gen == 0:
            self.__min = 0
            self.__max = 721

    def set_nat_dex(self, the_dex):
        self.__nat_dex = the_dex

    def get_nat_dex(self):
        return self.__nat_dex

    def set_local_dex(self, the_dex):
        self.__local_dex = the_dex

    def get_local_dex(self):
        return self.__local_dex

    def set_generation(self, the_gen):
        self.__generation = the_gen
        self.gen_decider()

    def get_generation(self):
        return self.__generation

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

    def print(self, the_gen, the_list):
        self.__my_printer.printer(the_gen, the_list)

    def web_scraper(self):
        print('Scraping Main')
        dex_data = []
        head = ['Number', 'Name', 'Type', '', 'Address', 'Species', 'Height', 'Weight', 'Local Number(s)']
        # print(dex_data)
        url = 'http://pokemondb.net/pokedex/'
        r = requests.get(url + 'national').text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = table.find_all('span')

        for card in cards:
            stuffs = card.find_all(['a', 'small'])
            dex_data.append([stuff.text for stuff in stuffs[1:4]])

        dex_data = self.__my_formatter.hash_stripper(dex_data)
        dex_data = self.__my_formatter.type_formatter(dex_data)
        dex_data = self.__my_formatter.add_url(dex_data, url)
        dex_data = self.__my_formatter.get_gen(dex_data, self.__min, self.__max)
        dex_data = self.scrape_additional(dex_data)
        # print(dex_data)
        dex_data.insert(0, head)

        self.set_local_dex(self.__my_formatter.formatter(dex_data))
        self.set_nat_dex(dex_data)

    @staticmethod
    def scrape_additional(the_list):
        print('Scraping additional')
        for datum in the_list:
            url = datum[4]
            print(datum[1])
            r = requests.get(url).text
            soup = BeautifulSoup(r, 'html.parser')
            vt = soup.find('table', attrs={'class': 'vitals-table'})
            rows = vt.find_all('td')

            indi = []
            for row in rows:
                indi.append(row.text)

            # datum.append(indi[0])
            datum.append(indi[2])
            datum.append(indi[3])
            datum.append(indi[4])
            datum.append(indi[6])

            # print('length: ', len(datum), 'The data: ', datum)

        return the_list
