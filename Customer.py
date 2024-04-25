import pyodbc

class Customer:
    def __init__(self, firstName, lastName, Age, Gender, phoneNumber, Email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        self.Gender = Gender
        self.phoneNumber = phoneNumber
        self.Email = Email
        self.password = password

PriceDict = {'Regular': 30, 'Premium': 50,'Standard':70, 'IMAX': 100}
#-------------------------------------------------------------------------------------------------
def create_customer_account(customer):
    cursor.execute("EXEC CreateCustomerAccount ?, ?, ?, ?, ?, ?, ?",
                   customer.Email, customer.firstName, customer.lastName, customer.Age,
                   customer.Gender, customer.phoneNumber, customer.password)
    cursor.commit()

def customer_login(email, password):
    cursor.execute("EXEC CustomerLogin ?, ?", email, password)
    count = cursor.fetchone()[0]
    return count == 1
#-------------------------------------------------------------------------------------------------

def ReserveTicket(customer,time,date,hallid,MovieName,seats,reservetype,paymenttype):
    cursor.execute("select Screen_type from Hall where Hall_Num = ?",hallid)
    screen_type = cursor.fetchone()[0]
    price = 0

    for seat in seats:
        cursor.execute("select SeatType from Seat where Seat_ID = ?",seat)
        seattype = cursor.fetchone()[0]
        price += PriceDict[seattype]+PriceDict[screen_type]
            
                
    sql_query = "DECLARE @Reserve_Id INT; EXEC ReserveTicket ?, ?, ?, ?, ?, ?, ?, ?, @Reserve_Id OUTPUT; SELECT @Reserve_Id"

    # Execute the stored procedure with parameters
    cursor.execute(sql_query, paymenttype, customer.Email, time, date, hallid, MovieName, price, reservetype)

    # Fetch the output parameter value (ReserveNo)
    ReserveId = cursor.fetchone()[0]

    # cursor.execute("EXEC ReserveTicket ?, ?, ?, ?, ?, ?, ?, ?", paymenttype, customer.Email,time, date, hallid, MovieName, price,reservetype)
    # ReserveId = cursor.fetchval()

    for seat in seats:
        cursor.execute("EXEC ReserveSeat ?, ?, ?, ?",ReserveId,seat,hallid)

    cursor.commit()


# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
cursor = conn.cursor()


customer = Customer(firstName='Mark', lastName='Salah', Age=19, Gender='Male',
                    phoneNumber='01110101010', Email='Mark.Saleh@gmail.com', password='145')

# create_customer_account(customer)

login_result = customer_login('Mark.Saleh@gmail.com', '145')
print("Login Successful!" if login_result else "Login Failed!")

ReserveTicket(customer,'20:00','2024-05-01',1,'The Avengers',[1,2,3,4],'Regular','Credit Card')

# Close the connection
conn.close()