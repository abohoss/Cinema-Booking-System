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

-------------------------------------------------Reserve Test-----------------------------------------------

EXEC dbo.ReserveTicket
		@Show_Time = '20:00' ,
        @Show_Date = '2024-05-01' ,
        @Hall_Id = 1 ,
        @MovieName = 'The Avengers' ,
        @Customer_Email = 'Yehiasakr@gmail.com' ,
		@PaymentType = 'Credit Card' ,
        @Reserveprice = 50 ,
        @Reservetype = 'Premium',
		@Seats = '1,2,3'

