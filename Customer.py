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
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
cursor = conn.cursor()


# customer = Customer(firstName='Mark', lastName='Salah', Age=19, Gender='Male',
#                     phoneNumber='01110101010', Email='Mark.Saleh@gmail.com', password='145')

# create_customer_account(customer)

login_result = customer_login('Mark.Saleh@gmail.com', '145')
print("Login Successful!" if login_result else "Login Failed!")

# Close the connection
conn.close()