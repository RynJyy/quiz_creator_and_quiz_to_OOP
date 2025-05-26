from quiz_creator import QuizCreator
from colorama import init

# Initialize colorama
init(autoreset=True)

if __name__ == "__main__":
    creator = QuizCreator()
    creator.run()