import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    if username == "Enmanuel" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Add code to open main application window here
        main_app = MainApplication(username)
        root.destroy()  # Close login window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

class MainApplication(tk.Tk):
    def __init__(self, username, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Porta del Sol Project")
        self.username = username
        
        # Set background color
        self.configure(bg="#ADD8E6")  # Light blue background color
        
        # Menu bar
        menubar = tk.Menu(self)
        
        # Home menu
        home_menu = tk.Menu(menubar, tearoff=0)
        home_menu.add_command(label="Home", command=self.open_home)
        home_menu.add_command(label="Settings", command=self.open_settings)
        home_menu.add_command(label="Notifications", command=self.open_notifications)
        menubar.add_cascade(label="Home", menu=home_menu)
        
        self.config(menu=menubar)
        
        # Company name label
        company_label = tk.Label(self, text="Porta del Sol Memorial Services, Inc.", font=("Helvetica", 16))
        company_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        
        # User name label
        user_label = tk.Label(self, text="Welcome, " + username, font=("Helvetica", 12))
        user_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        # Sign out button
        signout_button = tk.Button(self, text="Sign Out", command=self.sign_out)
        signout_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        
        # Tabs for different sections
        tabs = ["Customers", "Contracts", "Finance", "Cemetery", "Medical", "Demographic Registry", "Forensic Sciences Institute"]
        for i, tab in enumerate(tabs):
            button = tk.Button(self, text=tab, command=lambda t=tab: self.open_tab(t))
            button.grid(row=2, column=i, padx=10, pady=10)

    def open_home(self):
        # Implement functionality to open the home page
        print("Opening Home Page")
    
    def open_settings(self):
        # Implement functionality to open the settings page
        print("Opening Settings Page")
    
    def open_notifications(self):
        # Implement functionality to open the notifications page
        print("Opening Notifications Page")
    
    def sign_out(self):
        # Close the application window
        self.destroy()
    
    def open_tab(self, tab):
        # Implement functionality to open the selected tab
        print(f"Opening {tab} Tab")

# Create main login window
root = tk.Tk()
root.title("Porta del Sol Memorial Services, Inc.")
root.geometry("400x300")
root.configure(bg="#ADD8E6")  # Light blue background color

# Define font
font_style = ("Helvetica", 12)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", bg="#ADD8E6", fg="white", font=font_style)
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, bg="white", font=font_style)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", bg="#ADD8E6", fg="white", font=font_style)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, bg="white", show="*", font=font_style)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = tk.Button(root, text="Login", command=login, font=font_style)
login_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
