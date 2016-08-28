import pickle
import sys

class IO(object):
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

    @staticmethod
    def pickler(the_object):
        with open('test01.txt', 'wb') as f:
            pickle.dump(the_object, f)

    @staticmethod
    def load(the_file):
        with open(the_file, 'rb') as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def get_user_in(prompt):
        return input(prompt)
