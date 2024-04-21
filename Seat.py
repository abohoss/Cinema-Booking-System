import pyodbc

class Seat:
    def __init__(self, Row, seatNo,seatType):
        self.Row = Row
        self.seatNo = seatNo
        self.seatType = seatType
        self.booked = False

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Customer table
create_table_query = '''
    CREATE TABLE Seat (
    Row INT,
    SeatNo INT,
    SeatType VARCHAR(50),
    Hall_no INT,
    Booked BIT,
    
    PRIMARY KEY (Row, SeatNo, Hall_no),
    CONSTRAINT fk_hallid FOREIGN KEY (Hall_no) REFERENCES Hall(Hall_Num)
);
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()