import tkinter as tk
from tkinter import messagebox
import pyodbc
from Customer import customer_login
from Employee import employee_login

class CinemaHomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cinema Booking System")
        self.geometry("600x400")
        self.center_window()

        # Connect to the SQL database
        self.conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
        self.cursor = self.conn.cursor()

        # Create and place widgets
        self.create_widgets()

    def center_window(self):
        # Calculate x and y coordinates to center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = (screen_width - 600) // 2
        y_coordinate = (screen_height - 400) // 2

        # Set geometry to center the window
        self.geometry(f"600x400+{x_coordinate}+{y_coordinate}")

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self, text="Cinema Booking System", font=("Helvetica", 16, "bold italic"))
        title_label.pack(pady=20)

        # Middle labels
        middle_label1 = tk.Label(self, text="Welcome to Cinema Booking System", font=("Helvetica", 12))
        middle_label1.pack()
        middle_label2 = tk.Label(self, text="Press on Employee or Customer to continue.", font=("Helvetica", 12))
        middle_label2.pack()

        # Buttons
        emp_button = tk.Button(self, text="Employee", font=("Helvetica", 12), command=self.show_employee_login)
        emp_button.place(relx=0.2, rely=0.8, anchor=tk.CENTER)
        cust_button = tk.Button(self, text="Customer", font=("Helvetica", 12), command=self.show_customer_login)
        cust_button.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

    def show_employee_login(self):
        self.withdraw()  # Hide the home page
        emp_login_page = EmployeeLoginPage(self)
        emp_login_page.mainloop()

    def show_customer_login(self):
        self.withdraw()  # Hide the home page
        cust_login_page = CustomerLoginPage(self)
        cust_login_page.mainloop()

    def close_connection(self):
        # Close the connection
        self.cursor.close()
        self.conn.close()

class LoginPage(tk.Toplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.title(title)
        self.geometry("600x400")
        self.center_window()

        # Create and place widgets
        self.create_widgets()

    def center_window(self):
        # Calculate x and y coordinates to center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width - 600) // 2
        y_coordinate = (screen_height - 400) // 2

        # Set geometry to center the window
        self.geometry(f"600x400+{x_coordinate}+{y_coordinate}")

    def create_widgets(self):
        # Labels and Entry widgets for Login
        label_id = tk.Label(self, text="ID:", font=("Helvetica", 12))
        label_id.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        self.entry_id = tk.Entry(self, font=("Helvetica", 12))
        self.entry_id.grid(row=1, column=1, pady=10)

        label_password = tk.Label(self, text="Password:", font=("Helvetica", 12))
        label_password.grid(row=2, column=0, padx=20, pady=10, sticky='w')
        self.entry_password = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.entry_password.grid(row=2, column=1, pady=10)

        # Login and Back buttons
        login_button = tk.Button(self, text="Login", font=("Helvetica", 12), command=self.perform_login)
        login_button.grid(row=3, column=1, padx=20, pady=10, sticky='e')
        back_button = tk.Button(self, text="Back", font=("Helvetica", 12), command=self.back_to_home)
        back_button.grid(row=3, column=1, padx=20, pady=10, sticky='w')

    def back_to_home(self):
        self.destroy()  # Destroy the Login window
        self.master.deiconify()  # Show the Home page

class EmployeeLoginPage(LoginPage):
    def __init__(self, master):
        super().__init__(master, "Employee Login")

    def perform_login(self):
        # Retrieve ID and password
        emp_id = self.entry_id.get()
        password = self.entry_password.get()

        employee_login_result = employee_login(emp_id, password, self.master.cursor)
        if employee_login_result:
            messagebox.showinfo("Success", "Employee login successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

        # Clear entry fields
        self.entry_id.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        # Focus on ID entry field
        self.entry_id.focus_set()

class CustomerLoginPage(LoginPage):
    def __init__(self, master):
        super().__init__(master, "Customer Login")

    def perform_login(self):
        # Retrieve email and password
        email = self.entry_id.get()
        password = self.entry_password.get()

        customer_login_result = customer_login(email, password, self.master.cursor)
        if customer_login_result:
            messagebox.showinfo("Success", "Customer login successful!")
        else:
            messagebox.showerror("Error", "Invalid credentials. Please try again.")

        # Clear entry fields
        self.entry_id.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        # Focus on ID entry field
        self.entry_id.focus_set()

if __name__ == "__main__":
    home_page = CinemaHomePage()
    home_page.mainloop()
    home_page.close_connection()  # Close the database connection after closing the application
