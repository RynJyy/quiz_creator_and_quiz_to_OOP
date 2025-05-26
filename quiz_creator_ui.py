from colorama import Fore, init

init(autoreset=True)

def show_header():
    print(Fore.BLUE + "=" * 34)
    print(Fore.MAGENTA + "📚 Welcome to the quiz creator! 📚")
    print(Fore.BLUE + "=" * 34 + "\n")
    print(Fore.CYAN + "This program allows you to create your own quiz questions.")
    print(Fore.CYAN + "You can add questions, specify answers, and save them for later use.\n")
