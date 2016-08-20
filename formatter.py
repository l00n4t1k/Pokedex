from unidecode import unidecode

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
            new_url = the_url + datum[1]
            datum.append(unidecode(new_url))
        return the_list

    @staticmethod
    def get_gen(the_list, the_min, the_max):
        the_res = []
        for datum in the_list[the_min:the_max]:
            the_res.append(datum)
        return the_res

    @staticmethod
    def formatter(the_list):
        res = []
        cur_line = ''
        for datum in the_list[0:11]:
            # print(datum)
            cur_line = datum[0] + ', ' + datum[1] + ', ' + datum[2]
            if datum[3] != '':
                cur_line += '/' + datum[3]
            cur_line += ', ' + datum[4] + ', ' + datum[5] + ', ' + datum[6] + ', ' + datum[7] + ', ' + datum[8]
            res.append(cur_line)
        return res
