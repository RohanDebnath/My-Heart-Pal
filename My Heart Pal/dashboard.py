# dashboard.py
import tkinter as tk
from tkinter import messagebox
from chatbot import ChatGUI, Chatbot
import quiz
import analysis

class DashboardScreen(tk.Tk):
    def __init__(self, home_screen):
        super().__init__()
        self.title("Dashboard")
        self.geometry("400x200")
        self.state('zoomed')
        self.resizable(False, False)

        self.label = tk.Label(self, text="Welcome to Dashboard", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.chatbot_instance = Chatbot()

        self.chat_button = tk.Button(self, text="Chat With AI", command=self.open_chat)
        self.chat_button.pack(pady=5)

        self.quiz_button = tk.Button(self, text="Play quiz to know your heart better", command=self.open_quiz)
        self.quiz_button.pack(pady=5)

        self.analysis_button = tk.Button(self, text="Analysis of Heart by ML", command=self.open_analysis)
        self.analysis_button.pack(pady=5)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

        # Store a reference to the home screen to go back after logout
        self.home_screen = home_screen

    def open_chat(self):
        # Placeholder for opening chatbot.py
        self.withdraw()
        chat_gui = ChatGUI(tk.Tk(), self.chatbot_instance)
        chat_gui.master.protocol("WM_DELETE_WINDOW", lambda: self.on_chat_close(chat_gui))

    def open_quiz(self):
        # Placeholder for opening quiz.py
        self.withdraw()
        quiz_app = quiz.QuizApp(self)
        quiz_app.protocol("WM_DELETE_WINDOW", lambda: self.on_quiz_close(quiz_app))

    def open_analysis(self):
        # Placeholder for opening analysis.py
        self.withdraw()
        analysis_app = analysis.AnalysisApp(self)
        analysis_app.protocol("WM_DELETE_WINDOW", lambda: self.on_analysis_close(analysis_app))

    def on_chat_close(self, chat_gui):
        chat_gui.master.destroy()
        self.deiconify()

    def on_quiz_close(self, quiz_app):
        quiz_app.destroy()
        self.deiconify()

    def on_analysis_close(self, analysis_app):
        analysis_app.destroy()
        self.deiconify()

    def logout(self):
        # Close current window and go back to home screen
        self.withdraw()
        self.home_screen.deiconify()

if __name__ == "__main__":
    # For testing, pass a dummy HomeScreen instance
    home_screen = tk.Tk()  # Pass a dummy instance for testing
    app = DashboardScreen(home_screen)
    app.mainloop()
