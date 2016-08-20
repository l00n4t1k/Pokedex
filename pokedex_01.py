import requests
from bs4 import BeautifulSoup
import re
import csv


def printer(out_list):
    for datum in out_list:
        print(datum)


def scraper():
    dex_data = []
    num_list = []
    gen = 'G1'
    url = 'http://pokemondb.net/pokedex/national'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find('div', attrs={'class': 'infocard-tall-list'})
    cards = table.find_all('span')

    for card in cards[0:]:
        stuffs = card.find_all(['a', 'small'])
        dex_data.append([stuff.text for stuff in stuffs[1:4]])

    dex_data = hash_stripper(dex_data)
    dex_data = type_formatter(dex_data)
    out = formatter(dex_data)

    printer(out)


def hash_stripper(the_list):
    res = []
    for datum in the_list:
        datum[0] = datum[0].strip('#')
        res.append(datum)
    return res


def type_formatter(the_list):
    res = []
    tl = []
    for datum in the_list:
        # datum[2] = datum[2].replace(' · ', '/')
        # res.append(datum)
        if datum[2].find(' · ') == -1:
            datum.append('')
        else:
            tl = datum[2].split(' · ')
            datum[2] = tl[0]
            datum.append(tl[1])
        res.append(datum)
    return res


def formatter(the_list):
    cur_line = ''
    res = []
    for datum in the_list:
        cur_line = datum[0] + ', ' + datum[1] + ', ' + datum[2]
        if datum[3] != '':
            cur_line += '/' + datum[3]
        res.append(cur_line)
    return res

scraper()
