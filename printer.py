
class Printer(object):
    @staticmethod
    def printer(the_gen, the_list):
        print()
        print('-----------------------------------------')
        print()
        if the_gen != 0:
            print('Gen ', the_gen, ' List')
        else:
            print('All Pokemon')
        print('----------')
        for datum in the_list:
            print(datum)
