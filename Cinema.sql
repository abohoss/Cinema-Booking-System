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
      apartmentNumber INT,
      Password VARCHAR(100)
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
    Seat_ID Int,
    SeatType VARCHAR(50),
    Hall_no INT,
    Booked BIT,
    
    PRIMARY KEY (Seat_ID, Hall_no),
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
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    Price FLOAT,
    Transaction_Date DATE,
    PaymentType VARCHAR(50),
    Customer_Email VARCHAR(100),

    CONSTRAINT fk_Customer_Email FOREIGN KEY (Customer_Email) REFERENCES Customer(Email)
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
        Show_Time Time,
        Show_Date DATE,
        Hall_Id INT,
        MovieName VARCHAR(100),
        Customer_Email VARCHAR(100),
        price FLOAT,
        type VARCHAR(50),
        constraint pk_reserve primary key (Transaction_Id,Show_Time,Show_Date,Hall_Id,MovieName,Customer_Email),
        constraint fk_transactionid foreign key (Transaction_Id) references [Transaction](TransactionID),
        constraint fk_showtime foreign key (Show_Time,Show_Date,MovieName,Hall_Id) references ShowTime(Time,Date,Movie_Name,Hall_Number),
        constraint fk_email foreign key (Customer_Email) references Customer(Email),

);

CREATE TABLE ReservedSeats(
		TransactionId INT,
        ShowTime Time,
        ShowDate DATE,
        Hall_No INT,
        Movie_Name VARCHAR(100),
        CustomerEmail VARCHAR(100),
		Seat_No Int,
		Seat_Hall Int,
		primary key (TransactionId,ShowTime,ShowDate,Hall_No,Movie_Name,CustomerEmail,Seat_No,Seat_Hall),
		constraint fk_Reserve foreign key(TransactionId,ShowTime,ShowDate,Hall_No,Movie_Name,CustomerEmail) references Reserve(Transaction_Id,Show_Time,Show_Date,Hall_Id,MovieName,Customer_Email),
		constraint fk_seat foreign key (Seat_No,Seat_Hall) references Seat(Seat_ID,Hall_no),
);

Insert Into Hall  (Hall_Num,Screen_Type)
values (1,'Standard'),(2,'Standard'),(3,'IMAX'),(4,'IMAX')


-- Inserting data into the Seat table
INSERT INTO Seat (Seat_ID, SeatType, Hall_no, Booked)
VALUES
  -- First Hall
  (1,'Regular', 1, 0),(2,'Regular', 1, 0),(3,'Regular', 1, 0),(4,'Regular', 1, 0),(5,'Regular', 1, 0),
  (6,'Regular', 1, 0),(7,'Regular', 1, 0),(8,'Regular', 1, 0),(09,'Regular', 1, 0),(10,'Regular', 1, 0),
  (11,'Premium', 1, 0),(12,'Premium', 1, 0),(13,'Premium', 1, 0),(14,'Premium', 1, 0),(15,'Premium', 1, 0),
  (16,'Premium', 1, 0),(17,'Premium', 1, 0),(18,'Premium', 1, 0),(19,'Premium', 1, 0),(20,'Premium', 1, 0),
  
  -- Second Hall
  (1,'Regular', 2, 0),(2,'Regular', 2, 0),(3,'Regular', 2, 0),(4,'Regular', 2, 0),(5,'Regular', 2, 0),
  (6,'Regular', 2, 0),(7,'Regular', 2, 0),(8,'Regular', 2, 0),(09,'Regular', 2, 0),(10,'Regular', 2, 0),
  (11,'Premium', 2, 0),(12,'Premium', 2, 0),(13,'Premium', 2, 0),(14,'Premium', 2, 0),(15,'Premium', 2, 0),
  (16,'Premium', 2, 0),(17,'Premium', 2, 0),(18,'Premium', 2, 0),(19,'Premium', 2, 0),(20,'Premium', 2, 0),
  -- Third Hall
  (1,'Regular', 3, 0),(2,'Regular', 3, 0),(3,'Regular', 3, 0),(4,'Regular', 3, 0),(5,'Regular', 3, 0),
  (6,'Regular', 3, 0),(7,'Regular', 3, 0),(8,'Regular', 3, 0),(09,'Regular', 3, 0),(10,'Regular', 3, 0),
  (11,'Premium', 3, 0),(12,'Premium', 3, 0),(13,'Premium', 3, 0),(14,'Premium', 3, 0),(15,'Premium', 3, 0),
  (16,'Premium', 3, 0),(17,'Premium', 3, 0),(18,'Premium', 3, 0),(19,'Premium', 3, 0),(20,'Premium', 3, 0),
  -- Fourth Hall
  (1,'Regular', 4, 0),(2,'Regular', 4, 0),(3,'Regular', 4, 0),(4,'Regular', 4, 0),(5,'Regular', 4, 0),
  (6,'Regular', 4, 0),(7,'Regular', 4, 0),(8,'Regular', 4, 0),(09,'Regular', 4, 0),(10,'Regular', 4, 0),
  (11,'Premium', 4, 0),(12,'Premium', 4, 0),(13,'Premium', 4, 0),(14,'Premium', 4, 0),(15,'Premium', 4, 0),
  (16,'Premium', 4, 0),(17,'Premium', 4, 0),(18,'Premium', 4, 0),(19,'Premium', 4, 0),(20,'Premium', 4, 0)
    


