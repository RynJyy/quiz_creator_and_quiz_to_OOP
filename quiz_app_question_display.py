import tkinter as tk

class QuestionDisplay:
    def __init__(self, window):
        # Label to show the question text
        self.question_label = tk.Label(window, text="", wraplength=500, font=("Helvetica", 18, "bold"), bg="white", fg="black")
        self.question_label.pack(pady=30)

        # Label to show question category
        self.category_label = tk.Label(window, text="", font=("Helvetica", 12, "italic"), bg="white", fg="gray")
        self.category_label.pack()

        # Label to show difficulty level
        self.difficulty_label = tk.Label(window, text="", font=("Helvetica", 12, "italic"), bg="white", fg="gray")
        self.difficulty_label.pack(pady=(0, 20))

    def update(self, question):
        # Update labels with new question info
        self.question_label.config(text=question['question'])
        self.category_label.config(text=f"Category: {question.get('category', 'N/A')}")
        self.difficulty_label.config(text=f"Difficulty: {question.get('difficulty', 'N/A')}")
