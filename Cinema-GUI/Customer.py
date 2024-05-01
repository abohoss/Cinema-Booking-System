import pyodbc
import re


class Customer:
    def __init__(self, firstName, lastName, Age, Gender, phoneNumber, Email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        self.Gender = Gender
        self.phoneNumber = phoneNumber
        self.Email = Email
        self.password = password


PriceDict = {"Regular": 30, "Premium": 50, "Standard": 70, "IMAX": 100}


def validate_email(email):
    # Regular expression pattern for email validation
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the email matches the pattern
    if re.match(email_regex, email):
        return True
    else:
        return False


# -------------------------------------------------------------------------------------------------
def create_customer_account(customer, cursor):
    cursor.execute(
        "EXEC CreateCustomerAccount ?, ?, ?, ?, ?, ?, ?",
        customer.Email,
        customer.firstName,
        customer.lastName,
        customer.Age,
        customer.Gender,
        customer.phoneNumber,
        customer.password,
    )
    cursor.commit()


def customer_login(email, password, cursor):
    cursor.execute("EXEC CustomerLogin ?, ?", email, password)
    count = cursor.fetchone()[0]
    return count == 1


# -------------------------------------------------------------------------------------------------


def ReserveTicket(
    email, time, date, hallid, MovieName, seats, reservetype, paymenttype, cursor
):
    cursor.execute("SELECT Screen_type FROM Hall WHERE Hall_Num = ?", hallid)
    screen_type = cursor.fetchone()[0]
    price = 0
    seat_str = ",".join(str(seat) for seat in seats)
    for seat in seats:
        cursor.execute("SELECT SeatType FROM Seat WHERE Seat_ID = ?", seat)
        seattype = cursor.fetchone()[0]
        price += PriceDict[seattype] + PriceDict[screen_type]

    # Execute the SQL procedure
    cursor.execute(
        "EXEC ReserveTicket ?, ?, ?, ?, ?, ?, ?, ?, ?",
        time,
        date,
        hallid,
        MovieName,
        email,
        paymenttype,
        price,
        reservetype,
        seat_str,
    )

    # Commit the transaction
    cursor.commit()
    print("Reservation successful!")
    return price

def add_rating(movieName, email,rate, comment, cursor):
    cursor.execute("Exec addRating ?, ?, ?, ?",movieName, email, rate, comment)
    cursor.commit()


# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
# cursor = conn.cursor()


# customer = Customer(firstName='Mark', lastName='Salah', Age=19, Gender='Male',
#                     phoneNumber='01110101010', Email='Mark.Saleh@gmail.com', password='145')

# # create_customer_account(customer)

# # login_result = customer_login('Mark.Saleh@gmail.com', '145')
# # print("Login Successful!" if login_result else "Login Failed!")

# ReserveTicket(customer.Email,'20:00','2024-05-01',1,'The Avengers',[4],'Premium','Credit Card',cursor)

# # # Close the connection
# conn.close()
