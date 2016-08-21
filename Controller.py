import pickle as pickle


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
        try:
            self.my_scraper = self.load()
        except FileNotFoundError:
            self.my_scraper.set_generation(0)
            self.my_scraper.web_scraper()
        self.store()
        self.my_scraper.print(self.my_scraper.get_generation(), self.my_scraper.get_local_dex())

    def store(self):
        with open('test01.txt', 'wb') as f:
            pickle.dump(self.my_scraper, f)

    @staticmethod
    def load():
        with open('test01.txt', 'rb') as f:
            data = pickle.load(f)
        return data
