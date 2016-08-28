import csv
import IO
import sys
import re


class Controller(object):

    my_scraper = ''
    my_IO = ''
    full_dex = []

    def __init__(self, the_scraper, the_io):
        self.my_scraper = the_scraper
        self.my_IO = the_io

    def set_full_dex(self, the_dex):
        self.full_dex = the_dex

    def get_full_dex(self):
        self.full_dex = self.my_scraper.web_scrape()

    def ui_start(self):
        print(sys.argv)
        try:

            if len(sys.argv) > 1:

                for i in sys.argv:
                    if i.find('-g') > -1:
                        gen = IO.get_user_in("Enter the generation you want to see")
                        if gen.isdigit():
                            self.start()
        except AttributeError:
            print('enter an argument')
            # gen = self.my_IO.get_user_in("Enter the generation you want to see: ")
            # if gen.isdigit():
            #     self.start(gen)

    def start(self, the_gen):
        sel_dex = []
        f = self.my_scraper.get_formatter()
        x = self.my_IO
        try:
            self.my_scraper.set_nat_dex(x.load('test01.txt'))
        except FileNotFoundError:
            print("File not found. Performing fresh scrape")
            self.my_scraper.set_generation(0)
            self.my_scraper.web_scraper()
        except EOFError:
            self.my_scraper.set_generation(0)
            self.my_scraper.web_scraper()
        x.pickler(self.my_scraper.get_nat_dex())

        self.my_scraper.find_local_dex(the_gen)
        the_dex = self.my_scraper.get_local_dex()
        self.my_IO.printer(int(the_gen), f.readability_formatter(the_dex))

        """
        deprecated code - can possibly be deleted
        # for i in range(1, 2):
        #     self.my_scraper.set_generation(int(i))
        #     the_min = self.my_scraper.get_min()
        #     the_max = self.my_scraper.get_max()
        #     self.my_scraper.set_local_dex(f.readability_formatter(f.get_gen(self.my_scraper.get_nat_dex(), the_min,
        #                                                                     the_max)))
        # print(self.my_scraper.get_local_dex())
        # print(self.my_scraper.get_nat_dex())
        # print(self.my_scraper.get_formatter().readability_formatter(self.my_scraper.get_local_dex()))
        # print(f.csv_formatter(f.get_gen(self.my_scraper.get_nat_dex(), the_min, the_max)))
        # self.csv_save(f.csv_formatter(f.get_gen(self.my_scraper.get_nat_dex(), the_min, the_max)), i)
        # self.csv_save(self.my_scraper.get_local_dex(), i)
        # self.my_scraper.print(self.my_scraper.get_generation(), self.my_scraper.get_local_dex())
        # x.pickler(self.my_scraper.get_nat_dex())
        """
    """
    TODO
    get this working during the refactoring maybe?

    @staticmethod
    def csv_save(the_list, num):
        file = 'test0' + str(num) + '.csv'
        with open(file, 'w', newline='\r\n') as the_file:
            the_writer = csv.writer(the_file, delimiter=',')
            # for i in the_list:
            the_writer.writerow(the_list)
    """
