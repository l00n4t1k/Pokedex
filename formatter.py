from unidecode import unidecode
import re


class Formatter(object):

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

    @staticmethod
    def add_url(the_list, the_url):
        res = []
        for datum in the_list:
            if re.search('♀', datum[1]):
                datum[1] = 'Nidoran-f'
            elif re.search('♂', datum[1]):
                datum[1] = 'Nidoran-m'
            elif re.search('Farfetch\'d', datum[1]):
                datum[1] = 'Farfetchd'
            elif re.search('Mr. Mime', datum[1]):
                datum[1] = 'Mr-Mime'
            elif re.search('Mime Jr.', datum[1]):
                datum[1] = 'Mime-Jr'
            new_url = the_url + datum[1]
            # print('url append: ', datum[1])
            datum.append(unidecode(new_url))
        return the_list

    @staticmethod
    def accent_remover(i):
        # print(i)
        if i.find('Pokémon'):
            # print('found: ', i)
            i.replace('Pokémon', 'Pokemon')
        # print('accent remover')
        return i


    @staticmethod
    def get_gen(the_list, the_min, the_max):
        the_res = []
        for datum in the_list[the_min:the_max]:
            the_res.append(datum)
        return the_res

    @staticmethod
    def formatter(the_list):
        res = []
        head = ['Number', 'Name', 'Type', '', 'Address', 'Species', 'Height', 'Weight', 'Local Number(s)']
        the_list.insert(0, head)
        cur_line = ''
        for datum in the_list:
            # print(datum)
            cur_line = str(datum[0]) + ', ' + str(datum[1]) + ', ' + str(datum[2])
            if datum[3] != '':
                cur_line += '/' + str(datum[3])
            cur_line += ', ' + str(datum[4]) + ', ' + str(datum[5]) + ', ' + str(datum[6]) + ', ' + str(datum[7])\
                        + ', ' + str(datum[8])
            res.append(cur_line)
        return res
