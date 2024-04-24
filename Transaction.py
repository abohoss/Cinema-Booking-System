import pyodbc
class Transaction:
    def __init__(self, TransactionID, Price, Date, paymentType):
        self.TransactionID = TransactionID(unique=True)
        self.Price = Price
        self.Date = Date
        self.paymentType = paymentType
        

