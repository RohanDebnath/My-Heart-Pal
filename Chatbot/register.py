# register.py
import tkinter as tk
from tkinter import messagebox
import home

class RegisterScreen(tk.Tk):
    def __init__(self, home_screen):
        super().__init__()
        self.title("Register")
        self.geometry("300x150")

        self.label = tk.Label(self, text="Welcome to Registration Screen", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack(pady=5)

        self.home_button = tk.Button(self, text="Back to Home", command=self.back_to_home)
        self.home_button.pack(pady=5)

        self.home_screen = home_screen

    def register(self):
        # Placeholder for registration logic
        # For simplicity, store the username and password in a dictionary
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Registration Failed", "Username and password are required")
        else:
            messagebox.showinfo("Registration", "Registration successful!")
            self.withdraw()
            self.home_screen.deiconify()

    def back_to_home(self):
        self.withdraw()
        self.home_screen.deiconify()

if __name__ == "__main__":
    app = RegisterScreen(None)
    app.mainloop()
