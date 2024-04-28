import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtCore import Qt
from ui_form import Ui_MainWindow
from ui_empLogin import EmpLogin
from ui_userLogin import UserLogin
from ui_createAcc import CreateAccount
from ui_customerShowMovies import CustomerShowMovies
from Employee import employee_login
from Customer import customer_login
from Customer import create_customer_account
from Customer import Customer
from Movie import list_movies

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Establish database connection and save cursor
        self.conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-IG6PNT2};Database={Cinema}')
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

    def showReserveStub(self, movie_name):
        print(movie_name)

    def showCustomerShowMovies(self):
        self.ui = CustomerShowMovies()
        self.ui.setupUi(self)
        self.ui.signoutBtn.clicked.connect(self.backHome)

        # Add movies to moviesList QVBoxWidget
        for movie in list_movies(self.cursor):
            movie_card_widget = QWidget()
            movie_card = QVBoxLayout(movie_card_widget)
            # Movie image, Name, Genre, Cast
            info_layout_widget = QWidget()
            info_layout = QHBoxLayout(info_layout_widget)

            image = QLabel()
            image.setPixmap(QPixmap('images/imagePlaceholder.png').scaled(800, 150, Qt.KeepAspectRatio))
            info_layout.addWidget(image)

            info_text_layout_widget = QWidget()
            info_text_layout = QVBoxLayout(info_text_layout_widget)
            name = QLabel(movie.Name)
            name.setFont(QFont(str(QFont.Helvetica), 18, int(QFont.Bold)))
            name.setWordWrap(True)
            info_text_layout.addWidget(name)
            genre = QLabel(movie.Genre)
            genre.setWordWrap(True)
            info_text_layout.addWidget(genre)
            cast = QLabel(movie.Actors)
            cast.setFont(QFont(str(QFont.Helvetica), 9, int(QFont.Thin)))
            cast.setWordWrap(True)
            info_text_layout.addWidget(cast)
            info_text_layout.addStretch()
            info_layout.addWidget(info_text_layout_widget)

            reserve_btn = QPushButton(QIcon("images/book_online_FILL0_wght200_GRAD0_opsz20.png"), "Book Tickets")
            reserve_btn.clicked.connect(lambda checked, movie_name = movie.Name: self.showReserveStub(movie_name))
            info_layout.addWidget(reserve_btn)

            info_layout.addStretch()
            movie_card.addWidget(info_layout_widget)
            # Movie descritpion
            description = QLabel(movie.Description)
            description.setFont(QFont(str(QFont.Helvetica), 11))
            description.setWordWrap(True)
            movie_card.addWidget(description)
            # Add movie card to moviesList
            self.ui.moviesList.addWidget(movie_card_widget)
        self.ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


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
            self.showCustomerShowMovies()
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
