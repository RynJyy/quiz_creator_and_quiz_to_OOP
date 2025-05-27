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

    def next_question(self):
        if self.logic.is_finished():
            self.panel.show_final_score(self.logic.score, self.logic.total_questions)
            self.window.destroy()
            return

        question = self.logic.next_question()
        self.display.update(question)
        self.answers.set_answers(question['answers'], self.check_answer)
        self.panel.clear_feedback()

    def check_answer(self, answer):
        is_correct, correct_answer = self.logic.check_answer(answer)
        self.panel.show_feedback(is_correct, correct_answer)