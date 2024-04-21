import pyodbc
class Reserve:
    def __init__(self, customer,seat,transaction,showtime,price,type):
        self.customer = customer
        self.seat = seat
        self.transaction = transaction
        self.showtime = showtime
        self.price = price
        self.type = type

# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
CREATE TABLE Reserve (
        Transaction_id INT PRIMARY KEY,
        Seat_Row INT,
        Seat_Column INT,
        Show_Time VARCHAR(50),
        Show_Date DATE,
        Hall_id INT,
        Email VARCHAR(100),
        price FLOAT,
        type VARCHAR(50),

        constraint fk_transactionid foreign key (Transaction_id) references [Transaction](TransactionID),
        constraint fk_seat_row foreign key (Seat_Row) references Seat(Row),
        constraint fk_seat_column foreign key (Seat_Column) references Seat(SeatNo),
        constraint fk_show_time foreign key (Show_Time) references ShowTime(Time),
        constraint fk_show_date foreign key (Show_Date) references ShowTime(Date),
        constraint fk_hall_id foreign key (Hall_id) references Hall(Hall_No),
        constraint fk_email foreign key (Email) references Customer(Email)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close() 