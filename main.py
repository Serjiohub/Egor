import random
import time
import os
import sys
from colorama import Fore, init


class ColorWordsPrinter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        init(autoreset=True)

    def load_words(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.words = [line.strip() for line in f if line.strip()]

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def move_cursor(self, x, y):
        sys.stdout.write(f"\033[{y};{x}H")
        sys.stdout.flush()

    def print_words_randomly_forever(self, delay=1.5):
        if not self.words:
            self.load_words()

        while True:
            self.clear_console()
            columns, rows = os.get_terminal_size()

            for word in self.words:
                color = random.choice(self.colors)
                x = random.randint(1, max(1, columns - len(word)))
                y = random.randint(1, rows - 2)

                self.move_cursor(x, y)
                print(f"{color}{word}")

            time.sleep(delay)


if __name__ == "__main__":
    printer = ColorWordsPrinter("settings.txt")
    printer.print_words_randomly_forever()
