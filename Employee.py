import pyodbc
class Employee:
    def __init__(self,Fname,Lname,Emp_id,Salary,Role,Street_Name,Building_no,Apartment_no):
        self.Fname=Fname
        self.Lname=Lname
        self.Emp_id=Emp_id
        self.Salary=Salary
        self.Role=Role
        self.Street_Name=Street_Name
        self.Building_no=Building_no
        self.Apartment_no=Apartment_no
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
        CREATE TABLE Employee (
            Emp_id INT PRIMARY KEY,
            Fname VARCHAR(50),
            Lname VARCHAR(50),
            Salary DECIMAL(10, 2),
            Role VARCHAR(50),
            Street_Name VARCHAR(100),
            Building_no INT,
            Apartment_no INT
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()        
        