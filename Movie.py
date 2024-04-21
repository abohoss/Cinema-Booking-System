import pyodbc
class Movie:
    def __init__(self,Name,Description,Genre,Cast):
        self.Name = Name 
        self.Description = Description
        self.Genre = Genre
        self.Cast = Cast

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Movie table
create_table_query = '''
    CREATE TABLE Movie (
        
        VARCHAR(100) PRIMARY KEY,
        Description VARCHAR(255),
        Genre VARCHAR(50),
        Employee_Id INT,
        FOREIGN KEY (Employee_Id) REFERENCES Employee(Emp_Id)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()        
        