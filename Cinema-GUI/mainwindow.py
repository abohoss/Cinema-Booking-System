import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from ui_empLogin import EmpLogin
from ui_userLogin import UserLogin
from ui_createAcc import CreateAccount
from Employee import employee_login
from Customer import customer_login
from Customer import create_customer_account
from Customer import Customer

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Establish database connection and save cursor
        self.conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
        self.cursor = self.conn.cursor()

        self.email = None
        self.emp_id = None

        # Connect button clicks to appropriate slots
        self.ui.empBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.userBtn.clicked.connect(self.showUserLoginWindow)

    def showEmpLoginWindow(self):
        self.ui = EmpLogin()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.backHome)
        self.ui.loginBtn.clicked.connect(self.performEmpLogin)

    def showUserLoginWindow(self):
        self.ui = UserLogin()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.backHome)
        self.ui.loginBtn.clicked.connect(self.performUserLogin)
        self.ui.accBtn.clicked.connect(self.showCreateAccountWindow)  # Connect accBtn to showCreateAccountWindow

    def showCreateAccountWindow(self):
        self.ui = CreateAccount()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.showUserLoginWindow)  # Connect backBtn to showUserLoginWindow
        self.ui.createAccBtn.clicked.connect(self.performCreateAccount)

    def backHome(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.empBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.userBtn.clicked.connect(self.showUserLoginWindow)

    def performEmpLogin(self):
        # Retrieve text from QLineEdit widgets
        emp_id = self.ui.idField.text()
        password = self.ui.pField.text()

        # Call employee_login with retrieved values and cursor
        if employee_login(emp_id, password, self.cursor):
            self.emp_id = emp_id
            print("Success")
        else:
            print("No Employee with this id")  # Error Case

    def performUserLogin(self):
        # Retrieve text from QLineEdit widgets
        email = self.ui.emailField.text()
        password = self.ui.passField.text()

        # Call customer_login with retrieved values and cursor
        if customer_login(email, password, self.cursor):
            self.email = email
            print("Success")
        else:
            print("No Customer with this Email")  # Error Case

    def performCreateAccount(self):
        firstName = self.ui.fName.text()
        lastName = self.ui.lName.text()
        email = self.ui.emailField.text()
        age = (int(self.ui.ageField.text()))
        if self.ui.mRadio.isChecked():
            gender = "Male"
        elif self.ui.fRadio.isChecked():
            gender = "Female"
        else:
            print("Gender Error")
        phoneNumber = int(self.ui.phoneField.text())
        password = self.ui.password.text()
        customer = Customer(firstName,lastName,age,gender,phoneNumber,email,password)
        create_customer_account(customer,self.cursor)

    def closeEvent(self, event):
        # Close the database connection when the MainWindow is closed
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
