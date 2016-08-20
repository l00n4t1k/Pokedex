from controller import Controller
from scraper import Scraper
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from printer import Printer

f = Formatter
p = Printer
s = PokemonScraper(f, p)
c = Controller(s)
c.my_scraper.set_generation(6)
c.my_scraper.web_scraper()
# c.my_scraper.print(c.my_scraper.get_generation(), c.my_scraper.get_local_dex())
