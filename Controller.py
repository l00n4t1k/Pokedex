import sys
import re


class Controller(object):

    my_scraper = ''
    my_IO = ''
    my_cmd = ''
    full_dex = []
    local_dex = []

    def __init__(self, the_scraper, the_io):
        self.my_scraper = the_scraper
        self.my_IO = the_io
        # self.my_cmd = the_cmd

    def set_full_dex(self, the_dex):
        self.full_dex = the_dex

    def get_full_dex(self):
        self.full_dex = self.my_scraper.web_scrape()

    def set_local_dex(self, the_dex):
        self.local_dex = the_dex

    def get_local_dex(self):
        return self.local_dex

    def ui_start(self):
        if len(sys.argv) > 1:
            for i in sys.argv:
                if re.search('-g', i):
                    gen = self.my_IO.get_user_in("Enter the generation you want to see")
                    if gen.isdigit():
                        self.start(gen)
        else:
            pass

    def start(self, the_gen):
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
        self.full_dex = self.my_scraper.get_nat_dex()
        x.pickler(self.full_dex)

        self.my_scraper.find_local_dex(the_gen)
        the_dex = self.my_scraper.get_local_dex()
        self.my_IO.printer(int(the_gen), f.readability_formatter(the_dex))

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
