import pyodbc

class Employee:
    def __init__(self, Fname, Lname, Emp_id, Salary, Role, Street_Name, Building_no, Apartment_no):
        self.Fname = Fname
        self.Lname = Lname
        self.Emp_id = Emp_id
        self.Salary = Salary
        self.Role = Role
        self.Street_Name = Street_Name
        self.Building_no = Building_no
        self.Apartment_no = Apartment_no
#------------------------------------------------------------------------------------------------------------
def create_employee_account(employee):
    
    cursor.execute("EXEC CreateEmployeeAccount ?, ?, ?, ?, ?, ?, ?, ?",
                   employee.Emp_id, employee.Fname, employee.Lname, employee.Salary,
                   employee.Role, employee.Street_Name, employee.Building_no, employee.Apartment_no)
    cursor.commit()


# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
cursor = conn.cursor()

# employee = Employee(Fname='John', Lname='Doe', Emp_id=1, Salary=5000.00, Role='Manager',
#                     Street_Name='123 Main St', Building_no=1, Apartment_no=2)

# create_employee_account(employee)


# Close the connection
conn.close()