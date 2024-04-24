import pyodbc

class Reserve:
    def __init__(self, customer,seat,transaction,showtime):
        self.customer = customer
        self.seat = seat
        self.transaction = transaction
        self.showtime = showtime

