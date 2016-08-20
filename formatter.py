

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
    def formatter(the_list, min, max):
        res = []
        cur_line = ''
        for datum in the_list[min:max]:
            if int(datum[0]) > min:
                if int(datum[0]) <= max:
                    cur_line = datum[0] + ', ' + datum[1] + ', ' + datum[2]
                    if datum[3] != '':
                        cur_line += '/' + datum[3]
                else:
                    break
                res.append(cur_line)
        return res
