from quiz_creator_ui import UI
from quiz_creator_questions import QuizQuestion
from quiz_creator_storage import QuizStorage
from colorama import Fore

class QuizCreator:
    def __init__(self):
        self.storage = QuizStorage()  # Initialize storage handler

    def run(self):
        UI.show()  # Display welcome message and instructions
        while True:
            question = QuizQuestion()
            question.get_from_user()  # Prompt user to input question details
            self.storage.save_question(question.to_dict())  # Save question to JSON

            another = input(Fore.YELLOW + "Do you want to add another question? (yes/no): ").lower()
            if another != 'yes':
                print(Fore.BLUE + "Thank you for using the quiz creator, your file is now saved!")
                break  # Exit loop if user doesn’t want to add more questions
