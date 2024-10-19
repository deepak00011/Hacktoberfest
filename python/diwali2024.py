import time
import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def print_diya():
    print(f"{Fore.YELLOW}    ,    ")
    print(f"{Fore.YELLOW}   / \\   ")
    print(f"{Fore.YELLOW}  /   \\  ")
    print(f"{Fore.RED}  \\___/  ")

def print_firework(size):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    for i in range(size):
        print(" " * (size - i) + f"{random.choice(colors)}*" * (2 * i + 1))

def main():
    messages = [
        "Happy Diwali!",
        "May your life be as colorful as Rangoli!",
        "Let the light of the diyas guide you towards joy and prosperity!",
        "Wishing you a festival full of sweet moments and memories!"
    ]
    
    while True:
        print("\033[H\033[J")  # Clear the console
        print_diya()
        print()
        print(f"{Fore.CYAN}{Style.BRIGHT}{random.choice(messages)}")
        print()
        print_firework(random.randint(3, 6))
        time.sleep(1.5)

if __name__ == "__main__":
    main()