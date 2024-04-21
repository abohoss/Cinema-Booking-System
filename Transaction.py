import pyodbc
class Transaction:
    def __init__(self, TransactionID, Price, Date, paymentType):
        self.TransactionID = TransactionID(unique=True)
        self.Price = Price
        self.Date = Date
        self.paymentType = paymentType
        
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-T4EV4IC;Database=Cinema')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create the Employee table
create_table_query = '''
    CREATE TABLE [Transaction] (
        TransactionID INT PRIMARY KEY,
        Price Float,
        Date DATE,
        PaymentType VARCHAR(50)
    )
'''


cursor.execute(create_table_query)
conn.commit()

# Close the connection
conn.close() 
