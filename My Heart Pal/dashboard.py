# dashboard.py
import tkinter as tk

class DashboardScreen(tk.Tk):
    def __init__(self, home_screen):
        super().__init__()
        self.title("Dashboard")
        self.geometry("300x150")

        self.label = tk.Label(self, text="Welcome to Dashboard", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

        self.home_screen = home_screen

    def logout(self):
        self.withdraw()
        self.home_screen.deiconify()

if __name__ == "__main__":
    home_screen = home.HomeScreen()
    app = DashboardScreen(home_screen)
    app.mainloop()
