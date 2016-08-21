from controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from printer import Printer


s = PokemonScraper(Formatter, Printer)
c = Controller(s)
c.start()
