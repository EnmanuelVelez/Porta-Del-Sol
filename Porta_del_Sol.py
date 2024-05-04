import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
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
        self.configure(bg="#ADD8E6")
        
        menubar = tk.Menu(self)
        home_menu = tk.Menu(menubar, tearoff=0)
        home_menu.add_command(label="Home", command=self.open_home)
        home_menu.add_command(label="Settings", command=self.open_settings)
        home_menu.add_command(label="Notifications", command=self.open_notifications)
        menubar.add_cascade(label="Home", menu=home_menu)
        self.config(menu=menubar)

        company_label = tk.Label(self, text="Porta del Sol Memorial Services, Inc.", font=("Helvetica", 16))
        company_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        user_label = tk.Label(self, text="Welcome, " + username, font=("Helvetica", 12))
        user_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        signout_button = tk.Button(self, text="Sign Out", command=self.sign_out)
        signout_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

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

        add_button = tk.Button(self, text="Add Customer", command=self.add_customer)
        add_button.grid(row=1, column=0, pady=10)

        delete_button = tk.Button(self, text="Delete Customer", command=self.delete_customer)
        delete_button.grid(row=1, column=1, pady=10)

        self.load_customers()

    def load_customers(self):
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            # Clear existing entries
            for item in self.tree.get_children():
                self.tree.delete(item)

            cursor.execute("SELECT CustomerNum, CustomerID, CustomerFirstName, CustomerLastName, CustomerEmail, CustomerPhoneNumber FROM Customer")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error loading data", str(e))
        finally:
            cursor.close()
            conn.close()

    def add_customer(self):
        AddCustomerDialog(self)
        self.load_customers()  # Refresh the list after adding

    def delete_customer(self):
        selected_item = self.tree.selection()[0]
        customer_id = self.tree.item(selected_item)['values'][1]
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Customer WHERE [CustomerID] = ?", (customer_id,))
            conn.commit()
            self.tree.delete(selected_item)
            messagebox.showinfo("Success", "Customer deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", "Failed to delete customer")
        finally:
            cursor.close()
            conn.close()

class AddCustomerDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Customer Number:").grid(row=0)
        tk.Label(master, text="Customer ID:").grid(row=1)
        tk.Label(master, text="First Name:").grid(row=2)
        tk.Label(master, text="Last Name:").grid(row=3)
        tk.Label(master, text="Email:").grid(row=4)
        tk.Label(master, text="Phone Number:").grid(row=5)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e3 = tk.Entry(master)
        self.e4 = tk.Entry(master)
        self.e5 = tk.Entry(master)
        self.e6 = tk.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)

        return self.e1  # initial focus

    def apply(self):
        num = self.e1.get()
        cid = self.e2.get()
        fname = self.e3.get()
        lname = self.e4.get()
        email = self.e5.get()
        phone = self.e6.get()
        conn = connect_to_database()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Customer (CustomerNum, CustomerID, CustomerFirstName, CustomerLastName, CustomerEmail, CustomerPhoneNumber) VALUES (?, ?, ?, ?, ?, ?)", (num, cid, fname, lname, email, phone))
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully")
        except Exception as e:
            messagebox.showerror("Error", "Failed to add customer")
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
