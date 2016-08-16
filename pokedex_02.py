import requests
from bs4 import BeautifulSoup
import cmd
import string, sys
import re
import csv


class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '

    @staticmethod
    def do_hello(arg):
        print("hello again", arg, "!")

    @staticmethod
    def help_hello():
        print("syntax: hello [message]",)
        print("-- prints a hello message")

    @staticmethod
    def do_quit(arg):
        sys.exit(1)

    @staticmethod
    def help_quit():
        print("syntax: quit",)
        print("-- terminates the application")

    # shortcuts
    do_q = do_quit


class Scraper(object):

    __nat_dex = []
    __generation = 0
    __min = 0
    __max = 0

    def __init__(self, the_gen):
        self.set_generation(the_gen)
        self.gen_decider(the_gen)
        self.set_nat_dex(self.web_scraper())

    def printer(self):
        for datum in self.__nat_dex:
            print(datum)

    def gen_decider(self, gen):
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

        for card in cards[0:]:
            stuffs = card.find_all(['a', 'small'])
            dex_data.append([stuff.text for stuff in stuffs[1:4]])

        dex_data = self.hash_stripper(dex_data)
        dex_data = self.type_formatter(dex_data)
        out = self.formatter(dex_data)
        return out

    @staticmethod
    def hash_stripper(the_list):
        res = []
        for datum in the_list:
            datum[0] = datum[0].strip('#')
            res.append(datum)
        return res

    @staticmethod
    def type_formatter(the_list):
        res = []
        tl = []
        for datum in the_list:
            if datum[2].find(' · ') == -1:
                datum.append('')
            else:
                tl = datum[2].split(' · ')
                datum[2] = tl[0]
                datum.append(tl[1])
            res.append(datum)
        return res

    def formatter(self, the_list):
        res = []
        cur_line = ''
        for datum in the_list[self.__min:self.__max]:
            if int(datum[0]) > self.__min:
                if int(datum[0]) <= self.__max:
                    cur_line = datum[0] + ', ' + datum[1] + ', ' + datum[2]
                    if datum[3] != '':
                        cur_line += '/' + datum[3]
                else:
                    break
                res.append(cur_line)
        return res

scrape = Scraper(1)
print('Gen 1 List')
print('----------')
scrape.printer()

scrape = Scraper(2)
print()
print('-----------------------------------------')
print()
print('Gen 2 List')
print('----------')
scrape.printer()

scrape = Scraper(3)
print()
print('-----------------------------------------')
print()
print('Gen 3 List')
print('----------')
scrape.printer()

scrape = Scraper(4)
print()
print('-----------------------------------------')
print()
print('Gen 4 List')
print('----------')
scrape.printer()

scrape = Scraper(5)
print()
print('-----------------------------------------')
print()
print('Gen 5 List')
print('----------')
scrape.printer()

scrape = Scraper(6)
print()
print('-----------------------------------------')
print()
print('Gen 6 List')
print('----------')
scrape.printer()
