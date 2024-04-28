import sys
import pyodbc
import urllib.request
from datetime import datetime
from PySide6.QtCore import Qt, QDate, QTime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QFont, QIcon
from UI_.ui_form import Ui_MainWindow
from UI_.ui_empLogin import EmpLogin
from UI_.ui_userLogin import UserLogin
from UI_.ui_createAcc import CreateAccount
from UI_.ui_empHome import EmpHome
from UI_.ui_AddMovie import MovieAdd
from UI_.ui_RemoveMovie import RemoveMovie
from UI_.ui_AddShowTime import ShowAdd
from UI_.ui_ReserveView import ReserveView
from UI_.ui_RemoveShowTime import RemoveShowTime
from UI_.ui_customerShowMovies import CustomerShowMovies
from UI_.ui_success import Success
from UI_.ui_MovieRating import MovieRating
from Employee import employee_login
from Customer import customer_login , create_customer_account, ReserveTicket, Customer, validate_email, add_rating
from Movie import Movie,add_movie, list_movieNames, list_Halls, listMovieShowTimes,listMovieShowDates,listMovieShowHalls, getBookedSeats,delete_movie, list_movies
from Showtime import Showtime,add_showtime, delete_showtime, List_showtimes



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
        self.movieName = None



        # Connect button clicks to appropriate slots
        self.ui.empBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.userBtn.clicked.connect(self.showUserLoginWindow)

    def showEmpLoginWindow(self):
        self.emp_id = None
        self.ui = EmpLogin()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.backHome)
        self.ui.loginBtn.clicked.connect(self.performEmpLogin)

    def showUserLoginWindow(self):
        self.email = None
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

    def showSuccessWindow(self,price,Seats_List):
            self.ui = Success()
            self.ui.setupUi(self)
            self.ui.priceLabel.setText(f"Total Price: {price} EGP")
            self.ui.seatsLabel.setText(f"Seats: {Seats_List}")
            self.ui.returnBtn.clicked.connect(self.showCustomerShowMovies)  # Connect backBtn to showUserLoginWindow

    def showRating(self):
        self.ui=MovieRating()
        self.ui.setupUi(self)
        self.ui.Back.clicked.connect(self.showCustomerShowMovies)
        self.ui.confirm.clicked.connect(self.confirmRating)
        movie_names = list_movieNames(self.cursor)
        self.ui.name.clear()  # Clear the combobox before populating it
        for index, movie_name in enumerate(movie_names):
            self.ui.name.addItem(movie_name)
            self.ui.name.setItemData(index, movie_name)  # Set the data for each item
        self.ui.rating.clear()
        for index in range(0,6):
            self.ui.rating.addItem(str(index))
            self.ui.rating.setItemData(index,str(index))
    
    def confirmRating(self):
        Name = self.ui.name.currentData()
        rate = int(self.ui.rating.currentData())
        comm = self.ui.comment.text()
        if not comm:
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Comment Field is Empty")
            return
        try:
            add_rating(Name, self.email ,rate, comm, self.cursor)
            self.ui.label_6.setStyleSheet("color: green;")
            self.ui.label_6.setText("Rating Added Successfully")
        except:
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("You already rated the movie!")


    def setMovieName(self, movie_name):
        self.movieName = movie_name
        print(movie_name)
        self.showReserve()

    def showCustomerShowMovies(self):
        self.ui = CustomerShowMovies()
        self.ui.setupUi(self)
        self.ui.signoutBtn.clicked.connect(self.backHome)
        self.ui.rateBtn.clicked.connect(self.showRating)
        self.movieName = None

        # Add movies to moviesList QVBoxWidget
        for movie in list_movies(self.cursor):
            movie_card_widget = QWidget()
            movie_card = QVBoxLayout(movie_card_widget)
            # Movie image, Name, Genre, Cast
            info_layout_widget = QWidget()
            info_layout = QHBoxLayout(info_layout_widget)

            image = QLabel()
            data = urllib.request.urlopen(movie.image_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            image.setPixmap(pixmap.scaled(800, 150, Qt.KeepAspectRatio))
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
            reserve_btn.clicked.connect(lambda checked, movie_name = movie.Name: self.setMovieName(movie_name))
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

    def showEmpHome(self):
        self.ui=EmpHome()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.AddMovie.clicked.connect(self.showAddMovie)
        self.ui.removeMovie.clicked.connect(self.showRemoveMovie)
        self.ui.AddShow.clicked.connect(self.showAddShowTime)
        self.ui.removeShow.clicked.connect(self.showRemoveShowTime)

    def showReserve(self):
        self.ui = ReserveView()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.showCustomerShowMovies)

        hall_numbers = listMovieShowHalls(self.cursor,self.movieName)
        self.ui.hallnum.clear()  # Clear the combobox before populating it
        for index, hall_number in enumerate(hall_numbers):
            self.ui.hallnum.addItem(str(hall_number))
            self.ui.hallnum.setItemData(index, int(hall_number))  # Set the data as int
        self.updateShowDate()
        self.updateShowTime()
        self.ui.hallnum.currentIndexChanged.connect(self.updateShowDate)

        self.ui.date.currentIndexChanged.connect(self.updateShowTime)

        payment_types = ['Credit Card','Fawry','Cash']
        self.ui.ptype.clear()
        for index, type in enumerate(payment_types):
            self.ui.ptype.addItem(type)
            self.ui.ptype.setItemData(index, type)  # Set the data for each item
        if self.ui.hallnum.currentData() ==1 or self.ui.hallnum.currentData() ==2:
            self.ui.reserveType.setText('Standard')
        else:
            self.ui.reserveType.setText('IMAX')

        self.disableBookedSeats()
        self.ui.time.currentIndexChanged.connect(self.disableBookedSeats)
        self.ui.date.currentIndexChanged.connect(self.disableBookedSeats)
        self.ui.hallnum.currentIndexChanged.connect(self.disableBookedSeats)

        self.ui.hallnum.currentIndexChanged.connect(self.updateReserveType)
        self.ui.confirmBook.clicked.connect(self.reserveSeats)

    def updateShowTime(self):
        show_times = listMovieShowTimes(self.cursor,self.movieName,self.ui.hallnum.currentData(),self.ui.date.currentData())
        self.ui.time.clear()  # Clear the combobox before populating it
        for index, showtime in enumerate(show_times):
            self.ui.time.addItem(showtime)
            self.ui.time.setItemData(index, showtime)  # Set the data for each item

    def updateShowDate(self):
        show_dates = listMovieShowDates(self.cursor,self.movieName,self.ui.hallnum.currentData())
        self.ui.date.clear()  # Clear the combobox before populating it
        for index, showdate in enumerate(show_dates):
            self.ui.date.addItem(showdate)
            self.ui.date.setItemData(index, showdate)  # Set the data for each item
        self.updateShowTime()

    def updateReserveType(self, index):
        hall_id = self.ui.hallnum.currentData()
        if hall_id == 1 or hall_id == 2:
            reserve_type = 'Standard'
        else:
            reserve_type = 'IMAX'
        self.ui.reserveType.setText(reserve_type)

    def showAddMovie(self):
        self.ui=MovieAdd()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.confirmAddMovie)
        self.ui.Back.clicked.connect(self.showEmpHome)

    def showAddShowTime(self):
        self.ui = ShowAdd()
        self.ui.setupUi(self)
        self.ui.Add.clicked.connect(self.confirmAddShowTime)
        self.ui.Back.clicked.connect(self.showEmpHome)

        movie_names = list_movieNames(self.cursor)
        self.ui.name.clear()  # Clear the combobox before populating it
        for index, movie_name in enumerate(movie_names):
            self.ui.name.addItem(movie_name)
            self.ui.name.setItemData(index, movie_name)  # Set the data for each item

        hall_numbers = [num[0] for num in list_Halls(self.cursor)]
        self.ui.hallnum.clear()  # Clear the combobox before populating it
        for index, hall_number in enumerate(hall_numbers):
            self.ui.hallnum.addItem(str(hall_number))
            self.ui.hallnum.setItemData(index, int(hall_number))  # Set the data as int

    def showRemoveShowTime(self):
        self.ui = RemoveShowTime()
        self.ui.setupUi(self)
        self.ui.confirm.clicked.connect(self.confirmRemoveShowTime)
        self.ui.Back.clicked.connect(self.showEmpHome)
        shows = List_showtimes(self.cursor)
        self.ui.name.clear()
        self.ui.date.clear()
        self.ui.time.clear()
        self.ui.hallnum.clear()
        movieNames = set()
        halls = set()
        dates = set()
        times = set()
        for index, show in enumerate(shows):
            if show[0] not in times:
                self.ui.time.addItem(show[0])
                times.add(show[0])
                self.ui.time.setItemData(index, show[0])
            if show[1] not in dates:
                self.ui.date.addItem(show[1])
                dates.add(show[1])
                self.ui.date.setItemData(index, show[1])
            if show[2] not in movieNames:
                self.ui.name.addItem(show[2])
                movieNames.add(show[2])
                print(movieNames)
                self.ui.name.setItemData(index, show[2])
            if show[3] not in halls:
                self.ui.hallnum.addItem(str(show[3]))
                halls.add(show[3])
                self.ui.hallnum.setItemData(index, show[3])


    def showRemoveMovie(self):
        self.ui=RemoveMovie()
        self.ui.setupUi(self)
        self.ui.confirm.clicked.connect(self.confirmRemoveMovie)
        self.ui.Back.clicked.connect(self.showEmpHome)
        movie_names = list_movieNames(self.cursor)
        self.ui.name.clear()  # Clear the combobox before populating it
        for index, movie_name in enumerate(movie_names):
            self.ui.name.addItem(movie_name)
            self.ui.name.setItemData(index, movie_name)  # Set the data for each item


    def backHome(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.empBtn.clicked.connect(self.showEmpLoginWindow)
        self.ui.userBtn.clicked.connect(self.showUserLoginWindow)

    def confirmRemoveMovie(self):
        Name = self.ui.name.currentData()
        delete_movie(Name,self.cursor)
        self.ui.label_3.setStyleSheet("color: green;")
        self.ui.label_3.setText("Movie Removed Successfully")
        movie_names = list_movieNames(self.cursor)
        self.ui.name.clear()  # Clear the combobox before populating it
        for index, movie_name in enumerate(movie_names):
            self.ui.name.addItem(movie_name)
            self.ui.name.setItemData(index, movie_name)  # Set the data for each item

    def confirmRemoveShowTime(self):
        Name = self.ui.name.currentData()
        Date = self.ui.date.currentData()
        Time = self.ui.time.currentData()
        Hallno = self.ui.hallnum.currentData()
        delete_showtime(Time, Date, Name, Hallno, self.cursor)
        self.ui.label_7.setStyleSheet("color: green;")
        self.ui.label_7.setText("Showtime Removed Successfully")
        shows = List_showtimes(self.cursor)
        self.ui.name.clear()
        self.ui.date.clear()
        self.ui.time.clear()
        self.ui.hallnum.clear()
        movieNames = set()
        halls = set()
        dates = set()
        times = set()
        for index, show in enumerate(shows):
            if show[0] not in times:
                self.ui.time.addItem(show[0])
                times.add(show[0])
                self.ui.time.setItemData(index, show[0])
            if show[1] not in dates:
                self.ui.date.addItem(show[1])
                dates.add(show[1])
                self.ui.date.setItemData(index, show[1])
            if show[2] not in movieNames:
                self.ui.name.addItem(show[2])
                movieNames.add(show[2])
                print(movieNames)
                self.ui.name.setItemData(index, show[2])
            if show[3] not in halls:
                self.ui.hallnum.addItem(str(show[3]))
                halls.add(show[3])
                self.ui.hallnum.setItemData(index, show[3])

    def confirmAddMovie(self):
        Name = self.ui.name.text()
        if Name == "":
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please specify a name!")
            return
        Genre = self.ui.genre.text()
        if Genre == "":
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please specify a Genre!")
            return
        Desc = self.ui.description.toPlainText()
        if Desc == "":
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please specify a description!")
            return
        Cast = self.ui.cast.text()
        if Cast == "":
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please specify a Cast!")
            return
        image_url = self.ui.imageUrl.text()
        if image_url == "":
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please specify a Image url!")
        movie = Movie(Name,Desc,Genre,self.emp_id,image_url,Cast)
        try:
            add_movie(movie,self.cursor)
            self.ui.label_6.setStyleSheet("color: green;")
            self.ui.label_6.setText("Movie Added Successfully")
        except:
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Movie already exists")


    def confirmAddShowTime(self):
        Name = self.ui.name.currentData()
        print (Name)
        Hallno = self.ui.hallnum.currentData()
        
        # Get the selected time from the time edit
        time = self.ui.time.time()
        formatted_time = time.toString('hh:mm:ss')
        
        # Get the selected date from the date edit
        date = self.ui.date.date()
        current_date = QDate.currentDate()
        
        # Compare the selected date with the current date
        if date < current_date:
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Please select today or a future date!")
            return
        
        formatted_date = date.toString('yyyy-MM-dd')
        
        showtime = Showtime(formatted_time, formatted_date, Name, Hallno)
        try:
            add_showtime(showtime, self.cursor)
            self.ui.label_6.setStyleSheet("color: green;")
            self.ui.label_6.setText("Showtime Added Successfully")
        except:
            self.ui.label_6.setStyleSheet("color: red;")
            self.ui.label_6.setText("Show time already exists")


    def disableBookedSeats(self):
        ShowTime = self.ui.time.currentData()
        ShowDate = self.ui.date.currentData()
        HallId = self.ui.hallnum.currentData()
        for i in range(1, 21):
            seat_button = getattr(self.ui, f"seat{i}")
            seat_button.setEnabled(True)
            seat_button.setStyleSheet("")
        booked_Seats = getBookedSeats(self.cursor, self.movieName, ShowDate, ShowTime, HallId)
        # print(booked_Seats)
        if not booked_Seats:
            return
        for i in booked_Seats:
            seat_button = getattr(self.ui, f"seat{i}")
            seat_button.setEnabled(False)
            seat_button.setStyleSheet(
                "QPushButton {"
                "   background-color: white;"
                "   color: black;"
                "   border-radius: 10px;"
                "   padding: 5px;"
                "}"
            )



    def reserveSeats(self):
        ShowTime = self.ui.time.currentData()
        ShowDate = self.ui.date.currentData()
        HallId = self.ui.hallnum.currentData()
        paymentType = self.ui.ptype.currentData()
        if(HallId == 1 or HallId ==2):
            ReserveType = 'Standard'
        else:
            ReserveType = 'IMAX'

        Seats_List = []
        for i in range(1, 21):
            seat_button = getattr(self.ui, f"seat{i}")
            if seat_button.isChecked():
                Seats_List.append(str(i))

        if not Seats_List:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Please Select a Seat")
            return
                
        try:
            price = ReserveTicket(self.email,ShowTime,ShowDate,HallId,self.movieName,Seats_List,ReserveType,paymentType,self.cursor)
            self.ui.oLabel.setStyleSheet("color: green;")
            self.ui.oLabel.setText("Reservation Created Successfully")
            booked_Seats = getBookedSeats(self.cursor,self.movieName,ShowDate,ShowTime,HallId)
            for i in booked_Seats:
                seat_button = getattr(self.ui, f"seat{i}")
                seat_button.setEnabled(False)
            self.showSuccessWindow(price,Seats_List)
        except:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Seats Already Booked")


    def performEmpLogin(self):
        # Retrieve text from QLineEdit widgets
        emp_id = self.ui.idField.text()
        password = self.ui.pField.text()
        if not emp_id:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Id field is empty")
            return
        if not password:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Password field is empty")
            return
        # Call employee_login with retrieved values and cursor
        if employee_login(emp_id, password, self.cursor):
            self.emp_id = emp_id
            print("Success")
            self.showEmpHome()  # Call showEmpHome function
        else:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("No Employee with this Id")  # Error Case

    def performUserLogin(self):
        # Retrieve text from QLineEdit widgets
        email = self.ui.emailField.text()
        password = self.ui.passField.text()
        if not email:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Email field is empty")
            return
        if not (validate_email(email)):
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Email Format is Invalid")
            return

        if not password:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Password field is empty")
            return
        # Call customer_login with retrieved values and cursor
        if customer_login(email, password, self.cursor):
            self.email = email
            print("Success")
            self.showCustomerShowMovies()
        else:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("No User with this Email")

    def performCreateAccount(self):
        firstName = self.ui.fName.text()
        if not firstName:
               self.ui.oLabel.setStyleSheet("color: red;")
               self.ui.oLabel.setText("First Name field is empty")
               return
        lastName = self.ui.lName.text()
        if not lastName:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Last Name field is empty")
            return
        email = self.ui.emailField.text()
        if not email:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Email field is empty")
            return
        if not (validate_email(email)):
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Email Format is Invalid")
            return
        age = (self.ui.ageField.text())
        if not age:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Age field is empty")
            return
        age = int(age)

        if ((not (self.ui.mRadio.isChecked())) and (not (self.ui.fRadio.isChecked()))):
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Choose a gender")
            return

        if self.ui.mRadio.isChecked():
            gender = "Male"
        elif self.ui.fRadio.isChecked():
            gender = "Female"


        phoneNumber = self.ui.phoneField.text()
        if not phoneNumber:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Phone Number field is empty")
            return
        if len(phoneNumber) != 11:
                self.ui.oLabel.setStyleSheet("color: red;")
                self.ui.oLabel.setText("Phone Number must be 11 digits")
                return
        phoneNumber = int(phoneNumber)


        password = self.ui.password.text()
        if not password:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Password field is empty")
            return
        try:
            customer = Customer(firstName,lastName,age,gender,phoneNumber,email,password)
            create_customer_account(customer,self.cursor)
            self.ui.oLabel.setStyleSheet("color: green;")
            self.ui.oLabel.setText("Account Created Successfully")
            self.email = customer.Email
            self.showCustomerShowMovies()
        except:
            self.ui.oLabel.setStyleSheet("color: red;")
            self.ui.oLabel.setText("Email Already Exists")

    def closeEvent(self, event):
        # Close the database connection when the MainWindow is closed
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
