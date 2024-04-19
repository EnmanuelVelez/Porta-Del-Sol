import tkinter as tk
from tkinter import messagebox
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Add code to open main application window here
        open_main_application()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_main_application():
    # Create main application window
    main_window = tk.Tk()
    main_window.title("Main Application Window")
    main_window.geometry("400x400")

    # Run the Tkinter event loop for the main window
    main_window.mainloop()

# Create main login window
root = tk.Tk()
root.title("Portal del Sol Employee Portal")
root.geometry("400x300")
root.configure(bg="blue")

# Define font
font_style = ("Helvetica", 12)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", bg="blue", fg="white", font=font_style)
username_label.pack(pady=10)
username_entry = tk.Entry(root, bg="white", font=font_style)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", bg="blue", fg="white", font=font_style)
password_label.pack(pady=10)
password_entry = tk.Entry(root, bg="white", show="*", font=font_style)
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(root, text="Login", command=login, font=font_style)
login_button.pack(pady=10)

root.mainloop()
