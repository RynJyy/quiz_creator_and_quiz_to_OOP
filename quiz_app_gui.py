import tkinter as tk
from quiz_app_data_loader import QuizDataLoader
from quiz_app_logic import QuizLogic
from quiz_app_question_display import QuestionDisplay
from quiz_app_answer_buttons import AnswerButtons
from quiz_app_feedback import FeedbackPanel

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz App")  # Window title
        self.window.geometry("700x700")  # Window size
        self.window.configure(bg="white")  # Background color

        self.loader = QuizDataLoader()  # Load quiz data
        self.quiz_data = self.loader.load_data()
        if not self.quiz_data:  # Exit if no data
            return

        self.logic = QuizLogic(self.quiz_data)  # Quiz logic handler
        self.display = QuestionDisplay(self.window)  # Question display
        self.panel = FeedbackPanel(self.window, self.next_question)  # Feedback and controls
        self.answers = AnswerButtons(self.window, self.check_answer)  # Answer buttons

        self.next_question()  # Start quiz
        self.window.mainloop()

    def next_question(self):
        if self.logic.is_finished():  # End quiz if done
            self.panel.show_final_score(self.logic.score, self.logic.total_questions)
            self.window.destroy()
            return

        question = self.logic.next_question()  # Get next question
        self.display.update(question)  # Update display
        self.answers.set_answers(question['answers'], self.check_answer)  # Show answers
        self.panel.clear_feedback()  # Reset feedback

    def check_answer(self, answer):
        is_correct, correct_answer = self.logic.check_answer(answer)  # Check answer
        self.panel.show_feedback(is_correct, correct_answer)  # Show feedback
