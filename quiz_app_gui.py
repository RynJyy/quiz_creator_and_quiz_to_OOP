import tkinter as tk
from quiz_app_data_loader import QuizDataLoader
from quiz_app_logic import QuizLogic
from quiz_app_question_display import QuestionDisplay
from quiz_app_answer_buttons import AnswerButtons
from quiz_app_feedback import FeedbackPanel

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("✨ Quiz App ✨")
        self.window.geometry("700x700")
        self.window.configure(bg="white")

        self.loader = QuizDataLoader()
        self.quiz_data = self.loader.load_data()
        if not self.quiz_data:
            return

        self.logic = QuizLogic(self.quiz_data)
        self.display = QuestionDisplay(self.window)
        self.panel = FeedbackPanel(self.window, self.next_question)
        self.answers = AnswerButtons(self.window, self.check_answer)

        self.next_question()

        self.window.mainloop()