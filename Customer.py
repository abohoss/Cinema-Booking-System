import pyodbc
# class Customer:
#     def __init__(self,firstName,lastName,Age,Gender,phoneNumber,Email,password):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.Age = Age
#         self.Gender = Gender
#         self.phoneNumber = phoneNumber
#         self.Email = Email(unique=True)
#         self.password = password

# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

# # Create a cursor object to execute SQL statements
# cursor = conn.cursor()

# # Create the Customer table
# create_table_query = '''
#     CREATE TABLE Customer (
#         Email VARCHAR(100) PRIMARY KEY,
#         firstName VARCHAR(50),
#         lastName VARCHAR(50),
#         Age INT,
#         Gender VARCHAR(6),
#         phoneNumber VARCHAR(11),
#         Password VARCHAR(100)
#     )
# '''

# cursor.execute(create_table_query)
# conn.commit()

# # Close the connection
# conn.close()
    
def create_account(firstName, lastName, Age, Gender, phoneNumber, Email, password):
    conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

    cursor = conn.cursor()

    insert_query = '''
        INSERT INTO Customer (Email, firstName, lastName, Age, Gender, phoneNumber, Password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query, (Email, firstName, lastName, Age, Gender, phoneNumber, password))
    conn.commit()

    conn.close()

def login(email, password):
    
    conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')

    cursor = conn.cursor()

    select_query = '''
        SELECT * FROM Customer
        WHERE Email = ? AND Password = ?
    '''
    cursor.execute(select_query, (email, password))

    result = cursor.fetchone()

    conn.close()

    return result

create_account('Yehia', 'Sakr',19,'Male','01111831343','Yehiasakr@gmail.com','1234')
print(login('Yehiasakr@gmail.com','1234'))