from controller import Controller
from pokemon_scraper import PokemonScraper
from formatter import Formatter
from IO import IO


if __name__ == "__main__":
    s = PokemonScraper(Formatter)
    c = Controller(s, IO)
    c.start()
