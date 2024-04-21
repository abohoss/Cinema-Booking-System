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
        Transaction_Id INT PRIMARY KEY,
        Seat_Row INT,
        Seat_Column INT,
        Show_Time Time,
        Show_Date DATE,
        Hall_id INT,
        Customer_Email VARCHAR(100),
        price FLOAT,
        type VARCHAR(50),

        constraint fk_transactionid foreign key (Transaction_Id) references [Transaction](TransactionID),
        constraint fk_seat_row foreign key (Seat_Row) references Seat(Row),
        constraint fk_seat_column foreign key (Seat_Column) references Seat(SeatNo),
        constraint fk_show_time foreign key (Show_Time) references ShowTime(Time),
        constraint fk_show_date foreign key (Show_Date) references ShowTime(Date),
        constraint fk_hall_id foreign key (Hall_id) references Hall(Hall_Num),
        constraint fk_email foreign key (Customer_Email) references Customer(Email),

    )
'''

cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close()