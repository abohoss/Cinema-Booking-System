import pyodbc
class Manage_Halls:
    def __init__(self,Manager,Hall):
        self.Manager = Manager
        self.Hall =Hall
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
        CREATE TABLE Manage_Halls (
            Hall_Number INT,
            Manager_Id INT,
            PRIMARY KEY (Manager_Id, Hall_Number),
            FOREIGN KEY (Manager_Id) REFERENCES Employee(Emp_Id),
            FOREIGN KEY (Hall_Number) REFERENCES Hall(Hall_Num)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()    