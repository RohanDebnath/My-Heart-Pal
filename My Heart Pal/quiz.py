# quiz.py
import tkinter as tk
from tkinter import messagebox
import json

class QuizApp(tk.Tk):
    def __init__(self, dashboard_screen):
        super().__init__()
        self.title("Quiz")
        self.geometry("400x300")
        self.state('zoomed')  # Maximize the window
        self.resizable(False, False)  # Set resizable to False for both width and height

        self.dashboard_screen = dashboard_screen
        self.questions = self.fetch_questions()

        self.current_question_index = 0
        self.user_responses = []

        # Configure a larger font size
        self.font = ("Arial", 18)

        self.question_label = tk.Label(self, text="", font=self.font)
        self.question_label.pack(pady=20)

        self.yes_button = tk.Button(self, text="Yes", font=self.font, command=lambda: self.answer_question("yes"))
        self.yes_button.pack(pady=10)

        self.no_button = tk.Button(self, text="No", font=self.font, command=lambda: self.answer_question("no"))
        self.no_button.pack(pady=10)

        self.update_question()

    def fetch_questions(self):
        try:
            with open("questions.json", "r") as file:
                questions_data = json.load(file)
            return questions_data["questions"]
        except FileNotFoundError:
            print("Error: questions.json not found.")
            # Return sample questions for testing
            return [
                {"id": 1, "question": "Sample Question 1", "options": ["yes", "no"]},
                {"id": 2, "question": "Sample Question 2", "options": ["yes", "no"]},
                # Add more sample questions as needed
            ]

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_text = self.questions[self.current_question_index]["question"]
            self.question_label.config(text=question_text)
        else:
            self.show_result()

    def answer_question(self, response):
        self.user_responses.append(response)
        self.current_question_index += 1
        self.update_question()

    def show_result(self):
        total_responses = len(self.user_responses)
        yes_responses = self.user_responses.count("yes")
        percentage_yes = (yes_responses / total_responses) * 100 if total_responses > 0 else 0

        if percentage_yes > 80:
            messagebox.showinfo("Result", "Immediately Consult Doctor, your condition is worse")
        elif percentage_yes > 50:
            messagebox.showinfo("Result", "Please consult a doctor, as per your responses, you may have a heart disease")
        else:
            messagebox.showinfo("Result", "You are in good health!")

        # Go back to the dashboard
        self.withdraw()
        self.dashboard_screen.deiconify()

if __name__ == "__main__":
    # For testing, pass a dummy DashboardScreen instance
    dashboard_screen = tk.Tk()
    app = QuizApp(dashboard_screen)
    app.mainloop()
