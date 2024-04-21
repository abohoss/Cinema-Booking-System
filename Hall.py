import pyodbc
class Hall:
    def __init__(self,hall_no,screen_type,seats):
        self.hall_no =hall_no
        self.screen_type =screen_type
        self.seats =seats
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Hall table
create_table_query = '''
    CREATE TABLE Hall (
        Hall_Num INT PRIMARY KEY,
        Screen_Type VARCHAR(50)
    )
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()