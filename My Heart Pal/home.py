# home.py
import tkinter as tk
from tkinter import messagebox
import register
import dashboard

def authenticate(username, password):
    try:
        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if stored_username == username and stored_password == password:
                    return True
    except FileNotFoundError:
        return False
    return False

class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x150")
        self.state('zoomed')  # Maximize the window
        self.resizable(False, False)  # Set resizable to False for both width and height

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
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Login Failed", "Username and password are required")
        elif authenticate(username, password):
            self.withdraw()
            self.state('zoomed')  # Set the state to 'zoomed' when deiconifying
            dashboard.DashboardScreen(self)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register(self):
        self.withdraw()
        register.RegisterScreen(self)

if __name__ == "__main__":
    app = HomeScreen()
    app.mainloop()
