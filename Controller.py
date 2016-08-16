from scraper import Scraper
from formatter import Formatter


class Controller(object):

    _myScraper = ''
    _full_dex = []

    def __init__(self, the_scraper):
        self._myScraper = the_scraper

    def set_full_dex(self, the_dex):
        self._full_dex = the_dex

    def get_full_dex(self):
        self._full_dex = self._myScraper.web_scrape()

f = Formatter()
s = Scraper(f)
c = Controller(s)
s.set_generation(2)
s.gen_decider()
s.set_nat_dex(s.web_scraper())
s.printer()

