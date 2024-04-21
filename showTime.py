import pyodbc
class showTime:
    def __init__(self,Time, Date,Movie,Hall):
        self.Time=Time
        self.Date=Date
        self.Movie=Movie
        self.Hall=Hall

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
    CREATE TABLE ShowTime (
        Time TIME,
        Date DATE,
        Movie_Name VARCHAR(100),
        Hall_Num INT,
        PRIMARY KEY (Time, Date, Movie_Name,Hall_Num),
        FOREIGN KEY (Movie_Name) REFERENCES Movie(Name),
        FOREIGN KEY (Hall_Num) REFERENCES Hall(Hall_No)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close() 