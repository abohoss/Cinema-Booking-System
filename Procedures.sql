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
    -- Check if the customer already exists
    IF EXISTS (SELECT 1 FROM Customer WHERE Email = @Email)
    BEGIN
        -- Customer with the same email already exists, raise an error
        RAISERROR('Customer with the same email already exists', 16, 1);
        RETURN;
    END;

    -- Insert the customer into the Customer table
    INSERT INTO Customer (Email, firstName, lastName, Age, Gender, phoneNumber, Password)
    VALUES (@Email, @FirstName, @LastName, @Age, @Gender, @PhoneNumber, @Password);
END;
go

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
    @ApartmentNumber INT,
    @Password VARCHAR(100)
AS
BEGIN

        -- Check if the employee already exists
        IF EXISTS (SELECT 1 FROM Employee WHERE Emp_id = @EmpId)
        BEGIN
            RAISERROR('Employee with ID %d already exists.', 16, 1, @EmpId)
            RETURN;
        END

        -- Insert the employee record
        INSERT INTO Employee (Emp_id, firstName, lastName, Salary, Role, streetName, buildingNumber, apartmentNumber, Password)
        VALUES (@EmpId, @FirstName, @LastName, @Salary, @Role, @StreetName, @BuildingNumber, @ApartmentNumber, @Password);
END;
go
CREATE PROCEDURE EmployeeLogin
    @id INT,
    @Password VARCHAR(100)
AS
BEGIN

    SELECT COUNT(*) AS Count
    FROM Employee
    WHERE Emp_Id = @id AND Password = @Password;
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
------------------------------------------Movie/Halls Procedures----------------------------------------------------------------
CREATE PROCEDURE AddMovie
    @Name VARCHAR(100),
    @Description VARCHAR(255),
    @Genre VARCHAR(50),
    @EmployeeId INT,
    @Cast NVARCHAR(MAX)
AS
BEGIN
    -- Check if the movie already exists
    IF EXISTS (SELECT 1 FROM Movie WHERE Name = @Name)
    BEGIN
        -- Movie already exists, raise an error
        RAISERROR('Movie already exists', 16, 1);
        RETURN;
    END;

    -- Insert the movie into the Movie table
    INSERT INTO Movie (Name, Description, Genre, Employee_Id)
    VALUES (@Name, @Description, @Genre, @EmployeeId);

    -- Insert the cast members into the Cast table
    INSERT INTO Cast (MovieName, Actors)
    SELECT @Name, value
    FROM STRING_SPLIT(@Cast, ',');

END;
go

CREATE PROCEDURE ListMovies
AS
BEGIN
    SELECT M.Name, M.Description, M.Genre,
        STRING_AGG(C.Actors, ', ') AS Actors
    FROM Movie M
    JOIN Cast C ON M.Name = C.MovieName
    GROUP BY M.Name, M.Description, M.Genre;
END;
go

CREATE PROCEDURE ListMovieNames
AS
BEGIN
    SELECT Name from Movie       
END;
go
CREATE PROCEDURE ListMovieShowTimes
    @Name VARCHAR(100),
	@HallId INT,
	@Showdate date
AS
BEGIN
    SELECT CONVERT(VARCHAR(5), Time, 108) FROM ShowTime WHERE Movie_Name = @Name and Hall_Number = @HallId  and Date = @Showdate;
END;
CREATE PROCEDURE ListMovieShowDates
	@Name VARCHAR(100),
	@HallId int
AS
BEGIN
    SELECT Date from ShowTime where Movie_Name = @Name and Hall_Number = @HallId     
END;
go
CREATE PROCEDURE ListMovieShowHalls
	@Name VARCHAR(100)
AS
BEGIN
    SELECT Hall_Number from ShowTime where Movie_Name = @Name       
END;
go

CREATE PROCEDURE DeleteMovie
    @name VARCHAR(100)
AS
BEGIN
    UPDATE Seat SET Booked = 0 FROM Seat JOIN ReservedSeats ON Seat.Seat_ID = ReservedSeats.Seat_No AND Seat.Hall_no=ReservedSeats.Seat_Hall WHERE ReservedSeats.Movie_Name = @name;
    DELETE FROM Rate WHERE MovieName = @name;
    DELETE FROM Cast WHERE MovieName = @name;
    DELETE FROM ReservedSeats WHERE Movie_Name = @name; 
    DELETE FROM Reserve WHERE MovieName = @name;
    DELETE FROM ShowTime WHERE Movie_Name = @name;
    DELETE FROM Movie WHERE Name = @name;
END;
Exec DeleteMovie
@name = 'Se7en';
go
CREATE PROCEDURE selectMovie
    @name VARCHAR(100)
AS
BEGIN
    SELECT * FROM Movie WHERE Name = @name;
END;
GO
Exec selectMovie
@name = 'Se7en';
go
CREATE PROCEDURE ListHalls
AS
BEGIN
    SELECT Hall_Num from Hall       
END;
go
------------------------------------------Showtime Procedures----------------------------------------------------------------
CREATE PROCEDURE AddShowTime
  @Time TIME,
  @Date DATE,
  @MovieName VARCHAR(100),
  @HallNumber INT
AS
BEGIN
  -- Check if the ShowTime already exists
  IF EXISTS (
    SELECT 1
    FROM ShowTime
    WHERE Time = @Time
      AND Date = @Date
      AND Movie_Name = @MovieName
      AND Hall_Number = @HallNumber
  )
  BEGIN
    -- ShowTime already exists, raise an error
    RAISERROR('ShowTime already exists', 16, 1);
    RETURN;
  END;

  -- Insert the ShowTime into the ShowTime table
  INSERT INTO ShowTime (Time, Date, Movie_Name, Hall_Number)
  VALUES (@Time, @Date, @MovieName, @HallNumber);
END;

CREATE PROCEDURE DeleteShowTime
  @Time TIME,
  @Date DATE,
  @MovieName VARCHAR(100),
  @HallNumber INT
AS
BEGIN
    UPDATE Seat SET Booked = 0 FROM Seat JOIN ReservedSeats ON Seat.Seat_ID = ReservedSeats.Seat_No AND Seat.Hall_no=ReservedSeats.Seat_Hall WHERE ReservedSeats.ShowTime= @Time AND ReservedSeats.ShowDate=@Date AND ReservedSeats.Hall_No=@HallNumber AND ReservedSeats.Movie_Name=@MovieName;
    DELETE FROM ReservedSeats WHERE ShowTime= @Time AND ShowDate=@Date AND Hall_No=@HallNumber AND Movie_Name=@MovieName; 
    DELETE FROM Reserve WHERE Show_Time = @Time AND Show_Date= @Date AND MovieName=@MovieName AND Hall_Id= @HallNumber;
    DELETE FROM ShowTime WHERE Time = @Time AND Date = @Date AND Movie_Name = @MovieName AND Hall_Number = @HallNumber;
END;

EXEC DeleteShowTime
  @Time = '10:00:00.0000000',
  @Date = '2024-04-28',
  @MovieName = 'kheir w baraka',
  @HallNumber = '1';
  GO

CREATE PROCEDURE ListShowTimes
AS 
BEGIN
    SELECT CONVERT(VARCHAR(5), Time, 108), Date, Movie_Name, Hall_Number FROM ShowTime
END;
Exec ListShowTimes
Go
------------------------------------------Reserve+Transaction Procedure----------------------------------------------------------------
CREATE PROCEDURE ReserveTicket
    @Show_Time TIME,
    @Show_Date DATE,
    @Hall_Id INT,
    @MovieName VARCHAR(100),
    @Customer_Email VARCHAR(100),
    @PaymentType VARCHAR(50),
    @Reserveprice FLOAT,
    @Reservetype VARCHAR(50),
    @Seats VARCHAR(100)
AS
BEGIN
    DECLARE @TransactionId INT;

    -- Check if seat is already booked
    IF EXISTS (
        SELECT 1
        FROM Seat
        WHERE Seat_ID IN (
                SELECT CAST(Value AS INT)
                FROM STRING_SPLIT(@Seats, ',')
            )
            AND Hall_no = @Hall_Id
            AND Booked = 1
    )
    BEGIN
        -- Seat is already booked, return an error or take appropriate action
        RAISERROR('Selected seats are already booked. Reservation cannot be made.', 16, 1);
        RETURN;
    END;

    -- Insert into Transaction table
    INSERT INTO [Transaction] (Price, Transaction_Date, PaymentType, Customer_Email)
    VALUES (@ReservePrice, GETDATE(), @PaymentType, @Customer_Email);

    SET @TransactionId = SCOPE_IDENTITY(); -- Retrieve the automatically generated TransactionID

    -- Insert into Reserve table
    INSERT INTO Reserve (Transaction_Id, Show_Time, Show_Date, Hall_Id, MovieName, Customer_Email, price, type)
    VALUES (@TransactionId, @Show_Time, @Show_Date, @Hall_Id, @MovieName, @Customer_Email, @ReservePrice, @ReserveType);

    -- Split the comma-separated seat numbers into individual seats
    DECLARE @SeatList TABLE (Seat_No INT);
    DECLARE @SeatValue VARCHAR(10), @Pos INT, @Delimiter CHAR(1);

    SET @Delimiter = ',';
    SET @Seats = @Seats + @Delimiter;
    SET @Pos = CHARINDEX(@Delimiter, @Seats);

    WHILE @Pos > 0
    BEGIN
        SET @SeatValue = SUBSTRING(@Seats, 1, @Pos - 1);

        -- Convert seat value to INT and insert into the table variable
        INSERT INTO @SeatList (Seat_No)
        VALUES (CAST(@SeatValue AS INT));

        SET @Seats = SUBSTRING(@Seats, @Pos + 1, LEN(@Seats));
        SET @Pos = CHARINDEX(@Delimiter, @Seats);
    END;

    -- Insert reserved seats into the ReservedSeats table
    INSERT INTO ReservedSeats (TransactionId, ShowTime, ShowDate, Hall_No, Movie_Name, CustomerEmail, Seat_No, Seat_Hall)
    SELECT @TransactionId, @Show_Time, @Show_Date, @Hall_Id, @MovieName, @Customer_Email, Seat_No, @Hall_Id
    FROM @SeatList;

    -- Update the Seat table to mark the seats as booked
    UPDATE Seat
    SET Booked = 1
    WHERE Seat_ID IN (
            SELECT Seat_No
            FROM @SeatList
        )
        AND Hall_no = @Hall_Id;
END;

CREATE PROCEDURE GetBookedSeats
	@Movie_Name Varchar(100),
    @Show_Date DATE,
	@Show_Time TIME,
    @Hall_Id INT
AS
BEGIN
    SELECT Seat_No
    FROM ReservedSeats
    WHERE ShowTime = @Show_Time
        AND ShowDate = @Show_Date
        AND Hall_No = @Hall_Id;
END;
exec GetBookedSeats
	@Movie_Name = 'The Avengers',
	@Show_Date = '2024-05-25',
	@Show_Time = '00:00:00',
	@Hall_Id = 4
-------------------------------------------------Reserve Test-----------------------------------------------

EXEC dbo.ReserveTicket
		@Show_Time = '00:00' ,
        @Show_Date = '2024-05-25' ,
        @Hall_Id = 1 ,
        @MovieName = 'The Avengers' ,
        @Customer_Email = 'Yehiasakr@gmail.com' ,
		@PaymentType = 'Credit Card' ,
        @Reserveprice = 50 ,
        @Reservetype = 'Premium',
		@Seats = '18,20'

