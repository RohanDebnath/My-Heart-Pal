# home.py
import tkinter as tk
from tkinter import messagebox
import register
import dashboard

class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")

        self.label = tk.Label(self, text="Welcome to Home Screen", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(self, text="New User? Register", command=self.register)
        self.register_button.pack(pady=5)

    def login(self):
        # Placeholder for login logic
        # For demonstration purposes, accept any values
        self.withdraw()
        dashboard.DashboardScreen(self)

    def register(self):
        self.withdraw()
        register.RegisterScreen(self)

if __name__ == "__main__":
    app = HomeScreen()
    app.mainloop()
