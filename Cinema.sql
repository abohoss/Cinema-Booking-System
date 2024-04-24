create database Cinema;
use Cinema
go

CREATE TABLE Customer (
      Email VARCHAR(100) PRIMARY KEY,
      firstName VARCHAR(50),
      lastName VARCHAR(50),
      Age INT,
      Gender VARCHAR(6),
      phoneNumber VARCHAR(11),
      Password VARCHAR(100)
);

CREATE TABLE Employee (
      Emp_id INT PRIMARY KEY,
      firstName VARCHAR(50),
      lastName VARCHAR(50),
      Salary float,
      Role VARCHAR(50),
      streetName VARCHAR(100),
      buildingNumber INT,
      apartmentNumber INT
 );

 CREATE TABLE Movie (
      Name VARCHAR(100) PRIMARY KEY,
      Description VARCHAR(255),
      Genre VARCHAR(50),
      Employee_Id INT,
      FOREIGN KEY (Employee_Id) REFERENCES Employee(Emp_Id)
);

CREATE TABLE Cast (
    MovieName VARCHAR(100),
    Actors VARCHAR(200),
    constraint pk_cast primary key (MovieName,Actors),
    constraint fk_movieName foreign key (MovieName) references Movie(Name)
);

CREATE TABLE Hall (
    Hall_Num INT PRIMARY KEY,
    Screen_Type VARCHAR(50)
);

CREATE TABLE Seat (
    Row INT,
    SeatNo INT,
    SeatType VARCHAR(50),
    Hall_no INT,
    Booked BIT,
    
    PRIMARY KEY (Row, SeatNo, Hall_no),
    CONSTRAINT fk_hallid FOREIGN KEY (Hall_no) REFERENCES Hall(Hall_Num)
);

CREATE TABLE ShowTime (
    Time TIME,
    Date DATE,
    Movie_Name VARCHAR(100),
    Hall_Number INT,
    PRIMARY KEY (Time, Date, Movie_Name,Hall_Number),
    FOREIGN KEY (Movie_Name) REFERENCES Movie(Name),
    FOREIGN KEY (Hall_Number) REFERENCES Hall(Hall_Num)
);

CREATE TABLE [Transaction] (
    TransactionID INT PRIMARY KEY,
    Price Float,
    Transaction_Date DATE,
    PaymentType VARCHAR(50),
    Customer_Email VARCHAR(100),

    constraint fk_Customer_Email foreign key (Customer_Email) references Customer(Email)
);

CREATE TABLE Rate (
        MovieName VARCHAR(100),
        CustomerEmail VARCHAR(100),
        Rating INT CHECK (rating >= 0 AND rating <= 5),
        Comment VARCHAR(250),
        PRIMARY KEY (MovieName,CustomerEmail),
        FOREIGN KEY (MovieName) REFERENCES Movie(Name),
        FOREIGN KEY (CustomerEmail) REFERENCES Customer(Email)    
);

CREATE TABLE Manage_Halls (
    Hall_Number INT,
    Manager_Id INT,
    PRIMARY KEY (Manager_Id, Hall_Number),
    FOREIGN KEY (Manager_Id) REFERENCES Employee(Emp_Id),
    FOREIGN KEY (Hall_Number) REFERENCES Hall(Hall_Num)
);

CREATE TABLE Reserve (
        Transaction_Id INT,
        Seat_Row INT,
        Seat_Column INT,
        Show_Time Time,
        Show_Date DATE,
        Hall_Id INT,
        Seat_Hall INT,
        MovieName VARCHAR(100),
        Customer_Email VARCHAR(100),
        price FLOAT,
        type VARCHAR(50),
        constraint pk_reserve primary key (Transaction_Id,Seat_Row,Seat_Column,Show_Time,Show_Date,Hall_Id,Seat_Hall,MovieName,Customer_Email),
        constraint fk_transactionid foreign key (Transaction_Id) references [Transaction](TransactionID),
        constraint fk_seat foreign key (Seat_Row,Seat_Column,Seat_Hall) references Seat(Row,SeatNo,Hall_no),
        constraint fk_showtime foreign key (Show_Time,Show_Date,MovieName,Hall_Id) references ShowTime(Time,Date,Movie_Name,Hall_Number),
        constraint fk_email foreign key (Customer_Email) references Customer(Email),

);

Insert Into Hall  (Hall_Num,Screen_Type)
values (1,'Standard'),(2,'Standard'),(3,'IMAX'),(4,'IMAX')


-- Inserting data into the Seat table
INSERT INTO Seat (Row, SeatNo, SeatType, Hall_no, Booked)
VALUES
  -- First Hall
  (1, 1, 'Regular', 1, 0),(1, 2, 'Regular', 1, 0),(1, 3, 'Regular', 1, 0),(1, 4, 'Regular', 1, 0),(1, 5, 'Regular', 1, 0),
  (2, 1, 'Regular', 1, 0),(2, 2, 'Regular', 1, 0),(2, 3, 'Regular', 1, 0),(2, 4, 'Regular', 1, 0),(2, 5, 'Regular', 1, 0),
  (3, 1, 'Premium', 1, 0),(3, 2, 'Premium', 1, 0),(3, 3, 'Premium', 1, 0),(3, 4, 'Premium', 1, 0),(3, 5, 'Premium', 1, 0),
  (4, 1, 'Premium', 1, 0),(4, 2, 'Premium', 1, 0),(4, 3, 'Premium', 1, 0),(4, 4, 'Premium', 1, 0),(4, 5, 'Premium', 1, 0),
  
  -- Second Hall
  (1, 1, 'Regular', 2, 0),(1, 2, 'Regular', 2, 0),(1, 3, 'Regular', 2, 0),(1, 4, 'Regular', 2, 0),(1, 5, 'Regular', 2, 0),
  (2, 1, 'Regular', 2, 0),(2, 2, 'Regular', 2, 0),(2, 3, 'Regular', 2, 0),(2, 4, 'Regular', 2, 0),(2, 5, 'Regular', 2, 0),
  (3, 1, 'Premium', 2, 0),(3, 2, 'Premium', 2, 0),(3, 3, 'Premium', 2, 0),(3, 4, 'Premium', 2, 0),(3, 5, 'Premium', 2, 0),
  (4, 1, 'Premium', 2, 0),(4, 2, 'Premium', 2, 0),(4, 3, 'Premium', 2, 0),(4, 4, 'Premium', 2, 0),(4, 5, 'Premium', 2, 0),
  -- Third Hall
  (1, 1, 'Regular', 3, 0),(1, 2, 'Regular', 3, 0),(1, 3, 'Regular', 3, 0),(1, 4, 'Regular', 3, 0),(1, 5, 'Regular', 3, 0),
  (2, 1, 'Regular', 3, 0),(2, 2, 'Regular', 3, 0),(2, 3, 'Regular', 3, 0),(2, 4, 'Regular', 3, 0),(2, 5, 'Regular', 3, 0),
  (3, 1, 'Premium', 3, 0),(3, 2, 'Premium', 3, 0),(3, 3, 'Premium', 3, 0),(3, 4, 'Premium', 3, 0),(3, 5, 'Premium', 3, 0),
  (4, 1, 'Premium', 3, 0),(4, 2, 'Premium', 3, 0),(4, 3, 'Premium', 3, 0),(4, 4, 'Premium', 3, 0),(4, 5, 'Premium', 3, 0),
  -- Fourth Hall
  (1, 1, 'Regular', 4, 0),(1, 2, 'Regular', 4, 0),(1, 3, 'Regular', 4, 0),(1, 4, 'Regular', 4, 0),(1, 5, 'Regular', 4, 0),
  (2, 1, 'Regular', 4, 0),(2, 2, 'Regular', 4, 0),(2, 3, 'Regular', 4, 0),(2, 4, 'Regular', 4, 0),(2, 5, 'Regular', 4, 0),
  (3, 1, 'Premium', 4, 0),(3, 2, 'Premium', 4, 0),(3, 3, 'Premium', 4, 0),(3, 4, 'Premium', 4, 0),(3, 5, 'Premium', 4, 0),
  (4, 1, 'Premium', 4, 0),(4, 2, 'Premium', 4, 0),(4, 3, 'Premium', 4, 0),(4, 4, 'Premium', 4, 0),(4, 5, 'Premium', 4, 0)
    


