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
    -- Insert the movie into the Movie table
    INSERT INTO Movie (Name, Description, Genre, Employee_Id)
    VALUES (@Name, @Description, @Genre, @EmployeeId);

    -- Insert the cast members into the Cast table
    INSERT INTO Cast (MovieName, Actors)
    SELECT @Name, value
    FROM STRING_SPLIT(@Cast, ',');
END

CREATE PROCEDURE ListMovies
AS
BEGIN
    SELECT M.Name, M.Description, M.Genre,
        STRING_AGG(C.Actors, ', ') AS Actors
    FROM Movie M
    JOIN Cast C ON M.Name = C.MovieName
    GROUP BY M.Name, M.Description, M.Genre;
END
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
go
------------------------------------------Reserve+Transaction Procedures----------------------------------------------------------------
CREATE PROCEDURE ReserveTicket
  @PaymentType VARCHAR(50),
  @CustomerEmail VARCHAR(100),
  @ShowTime TIME,
  @ShowDate DATE,
  @HallId INT,
  @MovieName VARCHAR(100),
  @ReservePrice FLOAT,
  @ReserveType VARCHAR(50),
  @Reserve_No INT OUTPUT -- Output parameter to return Reserve_No
AS
BEGIN
  DECLARE @TransactionId INT;

  -- Insert into Transaction table
  INSERT INTO [Transaction] (Price, Transaction_Date, PaymentType, Customer_Email)
  VALUES (@ReservePrice, GETDATE(), @PaymentType, @CustomerEmail);

  SET @TransactionId = SCOPE_IDENTITY(); -- Retrieve the automatically generated TransactionID

  -- Insert into Reserve table
  INSERT INTO Reserve (Transaction_Id, Show_Time, Show_Date, Hall_Id, MovieName, Customer_Email, price, type)
  VALUES (@TransactionId, @ShowTime, @ShowDate, @HallId, @MovieName, @CustomerEmail, @ReservePrice, @ReserveType);

  SET @Reserve_No = SCOPE_IDENTITY(); -- Assign Reserve_No to output parameter
END;
go

create procedure ReserveSeat
	@ReserveID INT,
	@Seat_No INT,
	@Seat_Hall INT

AS
BEGIN
	INSERT INTO ReservedSeats(Reserve_ID,Seat_No,Seat_Hall)
	VALUES (@ReserveID,@Seat_No,@Seat_Hall)

	Update Seat 
		Set Booked = 1
	where Seat.Seat_ID = @Seat_No and Seat.Hall_no = @Seat_Hall
END;
go
-------------------------------------------------Reserve Test-----------------------------------------------
DECLARE @Reserve_Id INT;

EXEC dbo.ReserveTicket
    @PaymentType = 'Credit Card',
    @CustomerEmail= 'Yehiasakr@gmail.com',
    @ShowTime= '20:00',
    @ShowDate = '2024-05-01',
    @HallId = 1,
    @MovieName = 'The Avengers',
    @ReservePrice = 50,
    @ReserveType = 'Premium',
    @Reserve_No = @Reserve_Id OUTPUT;

SELECT @Reserve_Id AS ReserveId;


Exec dbo.ReserveSeat
	@ReserveID =@Reserve_Id,
	@Seat_No = 1,
	@Seat_Hall=1
