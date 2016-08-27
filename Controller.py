import pickle as pickle
import csv


class Controller(object):

    my_scraper = ''
    full_dex = []

    def __init__(self, the_scraper):
        self.my_scraper = the_scraper

    def set_full_dex(self, the_dex):
        self.full_dex = the_dex

    def get_full_dex(self):
        self.full_dex = self.my_scraper.web_scrape()

    def start(self):
        sel_dex = []
        f = self.my_scraper.get_formatter()
        try:
            self.my_scraper = self.load()
        except FileNotFoundError:
            print("File not found. Performing fresh scrape")
            self.my_scraper.set_generation(0)
            self.my_scraper.web_scraper()
        self.my_scraper.scrape_accent()
        for i in range(1, 7):
            self.my_scraper.set_generation(int(i))
            the_min = self.my_scraper.get_min()
            the_max = self.my_scraper.get_max()
            self.my_scraper.set_local_dex(f.readability_formatter(f.get_gen(self.my_scraper.get_nat_dex(), the_min,
                                                                            the_max)))
            print(self.my_scraper.get_local_dex())
            # print(self.my_scraper.get_formatter().readability_formatter(self.my_scraper.get_local_dex()))
            self.csv_save(f.csv_formatter(f.get_gen(self.my_scraper.get_nat_dex(), the_min, the_max)), i)
            # self.my_scraper.print(self.my_scraper.get_generation(), self.my_scraper.get_local_dex())
        self.store()

    def store(self):
        with open('test01.txt', 'wb') as f:
            pickle.dump(self.my_scraper, f)

    @staticmethod
    def load():
        with open('test01.txt', 'rb') as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def csv_save(the_list, num):
        file = 'test0' + str(num) + '.csv'
        with open(file, 'w', newline='\n') as the_file:
            the_writer = csv.writer(the_file, delimiter=':')
            for i in the_list:
                i += '\n'
                the_writer.writerow(str(i))
