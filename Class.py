import random
from colorama import Fore, Style, init

class ColorWordsPrinter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        init(autoreset=True)

    def load_words(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.words = [line.strip() for line in f if line.strip()]

    def print_colored_words(self):
        if not self.words:
            self.load_words()

        for word in self.words:
            color = random.choice(self.colors)
            print(f"{color}{word}")


if __name__ == "__main__":
    printer = ColorWordsPrinter("words.txt")
    printer.print_colored_words()