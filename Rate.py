import pyodbc
class Rate:
    def __init__(self,rating, comment,movie,customer):
        self.rating = rating
        self.comment = comment
        self.movie = movie
        self.customer = customer
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Hall table
create_table_query = '''
    CREATE TABLE Rate (
        MovieName VARCHAR(100),
        CustomerEmail VARCHAR(100),
        Rating INT CHECK (rating >= 0 AND rating <= 5),
        Comment VARCHAR(250),
        PRIMARY KEY (MovieName,CustomerEmail),
        FOREIGN KEY (MovieName) REFERENCES Movie(Name),
        FOREIGN KEY (CustomerEmail) REFERENCES Customer(Email)    
    )
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()