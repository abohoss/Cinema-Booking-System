import sys
import pyodbc
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from ui_empLogin import EmpLogin
from ui_userLogin import UserLogin
from ui_createAcc import CreateAccount
from ui_empHome import EmpHome
from ui_AddMovie import MovieAdd
from ui_RemoveMovie import RemoveMovie
from ui_AddShowTime import ShowAdd
from Employee import employee_login
from Customer import customer_login
from Customer import create_customer_account
from Customer import Customer
from Movie import Movie,add_movie
from Showtime import Showtime,add_showtime



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Establish database connection and save cursor
        self.conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-T4EV4IC};Database={Cinema}')
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

    def showEmpHome(self):
        self.ui=EmpHome()
        self.ui.setupUi(self)
        self.ui.AddMovie.clicked.connect(self.showAddMovie)
        self.ui.removeMovie.clicked.connect(self.showRemoveMovie)
        self.ui.AddShow.clicked.connect(self.showAddShowTime)
        # self.ui.removeShow.clicked.connect(self.showRemoveShowTime)

    def showAddMovie(self):
        self.ui=MovieAdd()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.confirmAddMovie)
        self.ui.Back.clicked.connect(self.showEmpHome)

    def showAddShowTime(self):
        self.ui=ShowAdd()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.confirmAddShowTime)
        self.ui.Back.clicked.connect(self.showEmpHome)

    def showRemoveMovie(self):
        self.ui=RemoveMovie()
        self.ui.setupUi(self)
        self.ui.confirm.clicked.connect(self.confirmRemoveMovie)

    def backHome(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.empBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.userBtn.clicked.connect(self.showUserLoginWindow)

    def confirmRemoveMovie(self):
        Name = self.ui.name.text()
        if Name == "":
            self.ui.label_6.setText("Please specify a name!")
            return;


    def confirmAddMovie(self):
        Name = self.ui.name.text()
        if Name == "":
            self.ui.label_6.setText("Please specify a name!")
            return;
        Genre = self.ui.genre.text()
        if Genre == "":
            self.ui.label_6.setText("Please specify a Genre!")
            return;
        Desc = self.ui.description.text()
        if Desc == "":
            self.ui.label_6.setText("Please specify a description!")
            return;
        Cast = self.ui.cast.text()
        if Cast == "":
            self.ui.label_6.setText("Please specify a Cast!")
            return;
        movie = Movie(Name,Desc,Genre,self.emp_id,Cast)
        add_movie(movie,self.cursor)
        print("added successfully")


    def confirmAddShowTime(self):
        Name = self.ui.name.text()
        if Name == "":
            self.ui.label_6.setText("Please specify a movie name!")
            return;
        date_string = self.ui.date.text()
        try:
            date = datetime.strptime(date_string, '%m/%d/%Y')
            formatted_date = date.strftime('%Y-%m-%d')
        except ValueError:
            print("The date string is not in the expected format.")
        if date_string == "":
            self.ui.label_6.setText("Please specify a date!")
            return;
        time_string = self.ui.time.text()
        try:
            time_obj = datetime.strptime(time_string, '%I:%M %p').time()
            formatted_time = time_obj.strftime('%H:%M:%S')
        except ValueError:
            print("The time string is not in the expected format.")
        if time_string == "":
            self.ui.label_6.setText("Please specify a time!")
            return;
        Hallno = self.ui.hallnum.text()
        if Hallno == "" or (int(Hallno) <= 0):
            self.ui.label_6.setText("Please specify a hall number!")
            return;
        Hallno = int(Hallno)
        showtime = Showtime(formatted_time,formatted_date,Name,Hallno)
        add_showtime(showtime,self.cursor)
        print("showtime added successfully!")

    def performEmpLogin(self):
        # Retrieve text from QLineEdit widgets
        emp_id = self.ui.idField.text()
        password = self.ui.pField.text()

        # Call employee_login with retrieved values and cursor
        if employee_login(emp_id, password, self.cursor):
            self.emp_id = emp_id
            self.ui.loginBtn.clicked.connect(self.showEmpHome)
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
