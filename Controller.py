class Controller(object):

    my_scraper = ''
    my_formatter = ''
    full_dex = []

    def __init__(self, the_scraper, the_formatter):
        self.my_scraper = the_scraper
        self.my_formatter = the_formatter

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
