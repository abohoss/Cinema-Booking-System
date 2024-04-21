import pyodbc
class Rate:
    def __init__(self,rating, comment,movie,customer):
        self.rating = rating
        self.comment = comment
        self.movie = movie
        self.customer = customer
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Hall table
create_table_query = '''
    CREATE TABLE Rate (
        rating INT CHECK (rating >= 0 AND rating <= 5),
        comment VARCHAR(250),
        MovieName VARCHAR(100),
        CustomerEmail VARCHAR(100),
        PRIMARY KEY (Name,Email),
        FOREIGN KEY (MovieName) REFERENCES Movie(Name),
        FOREIGN KEY (CustomerEmail) REFERENCES Customer(Email)    
    )
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()