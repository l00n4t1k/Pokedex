from cmd import Cmd


class Command(Cmd):
    """
    command line interface
    """
    intro = "HALP!!"
    prompt = "(> >_< <)"
    my_controller = None

    def __init__(self, the_controller):
        super(Command, self).__init__()
        # cmd.Cmd.__init__(self)
        self.my_controller = the_controller

    def set_controller(self, the_controller):
        self.my_controller = the_controller

    def do_new_scrape(self, line):
        """
        Perform a fresh web scrape of the entire pokedex
        """
        self.my_controller.my_scraper.set_generation(0)
        self.my_controller.my_scraper.web_scraper()

    def do_load(self, line):
        """
        Loads a pickled instance of a full national pokedex (all 721 Pokemon from the 6 generations)
        """
        file_name = input(">>> Enter the name of the pickled file to load: ")
        try:
            self.my_controller.my_scraper.set_nat_dex(self.my_controller.my_IO.load(file_name))
        except FileNotFoundError:
            res = input('File not found. Would you like to perform a fresh scrape "Y or N" ? ')
            if res.upper() == 'Y':
                self.do_new_scrape()

    def do_get_local_dex(self, line):
        """
        Creates a list of all the Pokemon from the entered generation
        """
        gen = input("Enter the generation number you want to search for: ")
        self.my_controller.set_local_dex(self.my_controller.my_scraper.find_local_dex(gen))

    def do_print_nat(self, line):
        """
        Prints the full national Pokedex of 721 Pokemon
        """
        self.my_controller.my_IO.printer(0, self.my_controller.my_scraper.get_formatter().readability_formatter(
            self.my_controller.my_scraper.get_nat_dex()))

    def do_print_local(self, line):
        """
        Prints the selected local Pokedex
        """
        self.my_controller.my_IO.printer(0, self.my_controller.my_scraper.get_formatter().readability_formatter(
            self.my_controller.get_local_dex()))

    @staticmethod
    def do_quit(line):
        """
        Exit the Program
        """
        print("Exiting.")
        return True
