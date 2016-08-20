class Controller(object):

    my_scraper = ''
    full_dex = []

    def __init__(self, the_scraper):
        self.my_scraper = the_scraper

    def set_full_dex(self, the_dex):
        self.full_dex = the_dex

    def get_full_dex(self):
        self.full_dex = self.my_scraper.web_scrape()

"""
s.set_generation(2)
s.gen_decider()
s.set_nat_dex(s.web_scraper())
s.printer()
"""
