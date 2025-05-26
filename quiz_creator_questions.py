from colorama import Fore

class QuizQuestion:
    def __init__(self):
        self.question = ""
        self.answers = []
        self.correct_answer = ""
        self.category = ""
        self.difficulty = ""

    def get_from_user(self):
            print(Fore.YELLOW + "\nEnter a new quiz question:")
            self.question = input(Fore.GREEN + "Question: ")

            self.answers = []
            for option in ['a', 'b', 'c', 'd']:
                answer = input(Fore.GREEN + f"Option {option}: ")
                self.answers.append(answer)

            while True:
                self.correct_answer = input(Fore.GREEN + "Correct answer (a/b/c/d): ").lower()
                if self.correct_answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter a, b, c, or d.")

            self.category = input(Fore.GREEN + "Category: ")

            while True:
                self.difficulty = input(Fore.GREEN + "Difficulty (intro/beginner/intermediate): ").lower()
                if self.difficulty in ['intro', 'beginner', 'intermediate']:
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter intro, beginner, or intermediate.")
    def to_dict(self):
            return {
                'question': self.question,
                'answers': self.answers,
                'correct_answer': self.correct_answer,
                'category': self.category,
                'difficulty': self.difficulty
            }
        