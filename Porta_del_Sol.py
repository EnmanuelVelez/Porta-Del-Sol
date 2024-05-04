import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

def connect_to_database():
    db_file = r"C:\Users\eliez\OneDrive\Escritorio\SICI Capstone Projecto Final\Porta del Sol\DatabaseSilverLight (1) (1).accdb"
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + db_file + ';'
    )
    return pyodbc.connect(conn_str)

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    if username == "Enmanuel" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        main_app = MainApplication(username)
        root.destroy()  # Close login window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

class MainApplication(tk.Tk):
    def __init__(self, username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Porta del Sol Project")
        self.username = username
        self.configure(bg="#ADD8E6")  # Light blue background color
        
        # Menu bar
        menubar = tk.Menu(self)
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
        print("Opening Home Page")
    
    def open_settings(self):
        print("Opening Settings Page")
    
    def open_notifications(self):
        print("Opening Notifications Page")
    
    def sign_out(self):
        self.destroy()
    
    def open_tab(self, tab):
        if tab == "Customers":
            CustomerWindow(self)
        else:
            print(f"Opening {tab} Tab")

class CustomerWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Customer Details")
        self.configure(bg="#ADD8E6")

        self.tree = ttk.Treeview(self, columns=("CustomerNum", "CustomerID", "CustomerFirstName", "CustomerLastName", "CustomerEmail", "CustomerPhoneNumber"), show="headings")
        self.tree.heading("CustomerNum", text="Customer Number")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("CustomerFirstName", text="First Name")
        self.tree.heading("CustomerLastName", text="Last Name")
        self.tree.heading("CustomerEmail", text="Email")
        self.tree.heading("CustomerPhoneNumber", text="Phone Number")
        self.tree.grid(row=0, column=0, sticky="nsew")

        self.load_customers()

    def load_customers(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT CustomerNum, CustomerID, CustomerFirstName, CustomerLastName, CustomerEmail, CustomerPhoneNumber FROM Customer")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error loading data", str(e))
        finally:
            cursor.close()
            conn.close()

# Create main login window
root = tk.Tk()
root.title("Porta del Sol Memorial Services, Inc.")
root.geometry("400x300")
root.configure(bg="#ADD8E6")

font_style = ("Helvetica", 12)
username_label = tk.Label(root, text="Username:", bg="#ADD8E6", fg="white", font=font_style)
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root, bg="white", font=font_style)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:", bg="#ADD8E6", fg="white", font=font_style)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, bg="white", show="*", font=font_style)
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login, font=font_style)
login_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
