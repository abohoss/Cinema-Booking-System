use Cinema
go
---------------------------------------CUSTOMER Procedures--------------------------------------------------
CREATE PROCEDURE CreateCustomerAccount
    @Email VARCHAR(100),
    @FirstName VARCHAR(50),
    @LastName VARCHAR(50),
    @Age INT,
    @Gender VARCHAR(6),
    @PhoneNumber VARCHAR(11),
    @Password VARCHAR(100)
AS
BEGIN

    INSERT INTO Customer (Email, firstName, lastName, Age, Gender, phoneNumber, Password)
    VALUES (@Email, @FirstName, @LastName, @Age, @Gender, @PhoneNumber, @Password);
END;
GO
CREATE PROCEDURE CustomerLogin
    @Email VARCHAR(100),
    @Password VARCHAR(100)
AS
BEGIN

    SELECT COUNT(*) AS Count
    FROM Customer
    WHERE Email = @Email AND Password = @Password;
END;
GO
---------------------------------------Employee Procedures--------------------------------------------------

CREATE PROCEDURE CreateEmployeeAccount
    @EmpId INT,
    @FirstName VARCHAR(50),
    @LastName VARCHAR(50),
    @Salary FLOAT,
    @Role VARCHAR(50),
    @StreetName VARCHAR(100),
    @BuildingNumber INT,
    @ApartmentNumber INT
AS
BEGIN

    INSERT INTO Employee (Emp_id, firstName, lastName, Salary, Role, streetName, buildingNumber, apartmentNumber)
    VALUES (@EmpId, @FirstName, @LastName, @Salary, @Role, @StreetName, @BuildingNumber, @ApartmentNumber);
END;
GO
------------------------------------------Test----------------------------------------------------------------
EXEC CreateCustomerAccount
    @Email = 'Yehiasakr@gmail.com',
    @FirstName = 'Yehia',
    @LastName = 'Sakr',
    @Age = 19,
    @Gender = 'Male',
    @PhoneNumber = '01111831343',
    @Password = '1234';
go
Exec CustomerLogin
	@Email = 'Yehiasakr@gmail.com',
	@Password = '1234';
go
------------------------------------------Movie Procedures----------------------------------------------------------------
CREATE PROCEDURE AddMovie
    @Name VARCHAR(100),
    @Description VARCHAR(255),
    @Genre VARCHAR(50),
    @EmployeeId INT,
    @Cast NVARCHAR(MAX)
AS
BEGIN
    INSERT INTO Movie (Name, Description, Genre, Employee_Id)
    VALUES (@Name, @Description, @Genre, @EmployeeId);

    INSERT INTO Cast (MovieName, Actors)
    VALUES (@Name, @Cast);
END
go

CREATE PROCEDURE ListMovies
AS
BEGIN
    SELECT M.Name, M.Description, M.Genre, C.Actors
    FROM Movie M
    JOIN Cast C ON M.Name = C.MovieName;
END
go
------------------------------------------Showtime Procedures----------------------------------------------------------------
CREATE PROCEDURE AddShowTime
  @Time TIME,
  @Date DATE,
  @MovieName VARCHAR(100),
  @HallNumber INT
AS
BEGIN
  INSERT INTO ShowTime (Time, Date, Movie_Name, Hall_Number)
  VALUES (@Time, @Date, @MovieName, @HallNumber);
END;
------------------------------------------Reserve+Transaction Procedures----------------------------------------------------------------
CREATE PROCEDURE ReserveTicket
  @TransactionDate DATE,
  @PaymentType VARCHAR(50),
  @CustomerEmail VARCHAR(100),
  @SeatRow INT,
  @SeatColumn INT,
  @ShowTime TIME,
  @ShowDate DATE,
  @HallId INT,
  @SeatHall INT,
  @MovieName VARCHAR(100),
  @ReservePrice FLOAT,
  @ReserveType VARCHAR(50)
AS
BEGIN
  DECLARE @TransactionId INT;

  -- Insert into Transaction table
  INSERT INTO [Transaction] (Price, Transaction_Date, PaymentType, Customer_Email)
  VALUES (@ReservePrice, @TransactionDate, @PaymentType, @CustomerEmail);

  SET @TransactionId = SCOPE_IDENTITY(); -- Retrieve the automatically generated TransactionID

  -- Insert into Reserve table
  INSERT INTO Reserve (Transaction_Id, Seat_Row, Seat_Column, Show_Time, Show_Date, Hall_Id, Seat_Hall, MovieName, Customer_Email, price, type)
  VALUES (@TransactionId, @SeatRow, @SeatColumn, @ShowTime, @ShowDate, @HallId, @SeatHall, @MovieName, @CustomerEmail, @ReservePrice, @ReserveType);
END;