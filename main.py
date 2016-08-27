from controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from printer import Printer


if __name__ == "__main__":
    s = PokemonScraper(Formatter, Printer)
    c = Controller(s)
    c.start()
