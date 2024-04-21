import pyodbc
class Seat:
    def __init__(self, Row, seatNo,seatType):
        self.Row = Row
        self.seatNo = seatNo
        self.seatType = seatType
        self.booked = False

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
    CREATE TABLE Seat (
        Row INT ,
        SeatNo INT ,
        SeatType VARCHAR(50),
        Hallid INT,
        Booked BIT,
        PRIMARY KEY(Row,SeatNo),
        constraint fk_hallid foreign key (Hallid) references Hall(Hall_No)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close() 
