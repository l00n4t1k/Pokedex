from controller import Controller
from scraper import Scraper
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from printer import printer

f = Formatter
s = Scraper(f)
c = Controller(s, f)
c.my_scraper.set_generation(2)
c.my_scraper.gen_decider()
temp_list = c.my_scraper.web_scraper()
printer(2, temp_list)
