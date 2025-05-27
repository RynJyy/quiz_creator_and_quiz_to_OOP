import tkinter as tk

class AnswerButtons:
    def __init__(self, window, on_answer):
        # List to hold the four answer buttons
        self.buttons = []
        # Create 4 buttons and add them to the window
        for i in range(4):
            btn = tk.Button(
                window, text="", width=30, height=2,
                font=("Helvetica", 12), fg="black",
                bg="white", relief="ridge"
            )
            btn.pack(pady=8)  # Add vertical padding between buttons
            self.buttons.append(btn)  # Save button reference
        # Callback function to handle answer selection
        self.on_answer = on_answer

    def set_answers(self, answers, correct_callback):
        # Set the text and command for each button based on answers
        # 'option' represents answer key: 'a', 'b', 'c', 'd'
        for i, option in enumerate(['a', 'b', 'c', 'd']):
            self.buttons[i].config(
                text=answers[i],  # Display answer text on button
                command=lambda opt=option: self.on_answer(opt),  # Call callback on click
                bg="white",  # Reset button background color
                activebackground="#d9d9d9"  # Button color when clicked/active
            )