
class Customer:
    def __init__(self,firstName,lastName,Age,Gender,phoneNumber,Email,password):
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        self.Gender = Gender
        self.phoneNumber = phoneNumber
        self.Email = Email(unique=True)
        self.password = password

    
    