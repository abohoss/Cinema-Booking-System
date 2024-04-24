import pyodbc

class Seat:
    def __init__(self, Row, seatNo,seatType):
        self.Row = Row
        self.seatNo = seatNo
        self.seatType = seatType
        self.booked = False
