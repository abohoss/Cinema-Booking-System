import pyodbc

class Reserve:
    def __init__(self, customer,seat,transaction,showtime):
        self.customer = customer
        self.seat = seat
        self.transaction = transaction
        self.showtime = showtime

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Customer table
create_table_query = '''
    CREATE TABLE Reserve (
        Transaction_Id INT,
        Seat_Row INT,
        Seat_Column INT,
        Show_Time Time,
        Show_Date DATE,
        Hall_Id INT,
        Seat_Hall INT,
        MovieName VARCHAR(100),
        Customer_Email VARCHAR(100),
        price FLOAT,
        type VARCHAR(50),
        constraint pk_reserve primary key (Transaction_Id,Seat_Row,Seat_Column,Show_Time,Show_Date,Hall_Id,Seat_Hall,MovieName,Customer_Email),
        constraint fk_transactionid foreign key (Transaction_Id) references [Transaction](TransactionID),
        constraint fk_seat foreign key (Seat_Row,Seat_Column,Seat_Hall) references Seat(Row,SeatNo,Hall_no),
        constraint fk_showtime foreign key (Show_Time,Show_Date,MovieName,Hall_Id) references ShowTime(Time,Date,Movie_Name,Hall_Number),
        constraint fk_email foreign key (Customer_Email) references Customer(Email),

    )
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()