import tkinter as tk
from tkinter import messagebox

class FeedbackPanel:
    def __init__(self, window, on_next):
        self.result_label = tk.Label(window, text="", font=("Helvetica", 16, "bold"), bg="white", fg="black")
        self.result_label.pack(pady=15)

        self.next_button = tk.Button(window, text="Next", command=on_next, bg="white", fg="black",
                                     font=("Helvetica", 12, "bold"), width=15, height=2, relief="ridge")
        self.next_button.pack(pady=20)
        self.next_button.config(state=tk.DISABLED)

        self.exit_button = tk.Button(window, text="Exit Quiz", command=window.destroy, bg="white", fg="black",
                                     font=("Helvetica", 12, "bold"), width=15, height=2, relief="ridge")
        self.exit_button.pack(pady=20)