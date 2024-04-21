import pyodbc
class Transaction:
    def __init__(self, TransactionID, Price, Date, paymentType):
        self.TransactionID = TransactionID(unique=True)
        self.Price = Price
        self.Date = Date
        self.paymentType = paymentType
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
    CREATE TABLE [Transaction] (
        TransactionID INT PRIMARY KEY,
        Price Float,
        Transaction_Date DATE,
        PaymentType VARCHAR(50),
        Customer_Email VARCHAR(100),

        constraint fk_Customer_Email foreign key (Customer_Email) references Customer(Email)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close() 
