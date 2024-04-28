import pyodbc

class Movie:
    def __init__(self, Name, Description, Genre, EmpId, Cast):
        self.Name = Name
        self.Description = Description
        self.Genre = Genre
        self.EmpId = EmpId
        self.Cast = Cast

def add_movie(movie,cursor):
        cursor.execute("EXEC AddMovie ?, ?, ?, ?, ?", movie.Name, movie.Description, movie.Genre, movie.EmpId, movie.Cast)
        cursor.commit()

def list_movies(cursor):
        cursor.execute("EXEC ListMovies")

        rows = cursor.fetchall()
        for row in rows:
            print("Movie Name:", row.Name)
            print("Description:", row.Description)
            print("Genre:", row.Genre)
            print("Cast Members:", row.Actors)
            print("-" * 50)

def list_movieNames(cursor):
        cursor.execute("Exec ListMovieNames")
        rows = cursor.fetchall()
        movie_names = []
        for row in rows:
                movie_names.append(row.Name)
        return movie_names
    
def list_Halls(cursor):
        cursor.execute("Exec ListHalls")
        rows = cursor.fetchall()
        hall_nums = []
        for row in rows:
                hall_nums.append(row)
        return hall_nums

def delete_movie(name, cursor):
        cursor.execute("Exec DeleteMovie ?",name)
        cursor.commit()

def listMovieShowTimes(cursor, movie_name, hall_num, show_date):
    cursor.execute("Exec ListMovieShowTimes ?,?,?", movie_name, hall_num, show_date)
    rows = cursor.fetchall()
    show_times = []
    for row in rows:
        show_time = row[0]  # Extract the time value
        show_times.append(show_time)
    # print(show_times)
    return show_times

def listMovieShowDates(cursor, movie_name,Hall_num):
    cursor.execute("Exec ListMovieShowDates ?,?", movie_name,Hall_num)
    rows = cursor.fetchall()
    show_dates = []
    for row in rows:
        show_date = row[0]  # Extract the date value
        show_dates.append(show_date)
    show_dates = list(set(show_dates))  # Convert to set and back to list to remove duplicates
    show_dates.sort()
    # print(show_dates)
    return show_dates

def listMovieShowHalls(cursor, movie_name):
    cursor.execute("Exec ListMovieShowHalls ?", movie_name)
    rows = cursor.fetchall()
    show_hall = []
    for row in rows:
        show_hall_num = row[0]  # Extract the hall value
        show_hall.append(show_hall_num)
    show_hall = list(set(show_hall))  # Convert to set and back to list to remove duplicates
    show_hall.sort()
    return show_hall

def getBookedSeats(cursor, movie_name, show_date, show_time, hall_num):
    cursor.execute("Exec GetBookedSeats ?, ?, ?, ?", movie_name, show_date, show_time, hall_num)
    rows = cursor.fetchall()
    booked_seats = []
    for row in rows:
        booked_seats.append(row[0])
    booked_seats.sort()
    # print(booked_seats)
    return booked_seats
# # # ---------------------------------------------------------------------------------------------------------------------------#
# Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
# cursor = conn.cursor()

# # movie = Movie(Name='Thor', Description='Superhero movie', Genre='Action', EmpId=1, Cast='Chris Hemsworth, Tom Hiddleston, Natalie Portman, Anthony Hopkins')
# # add_movie(movie,cursor)

# # list_movies()
# # list_movieNames(cursor)
# # list_Halls(cursor)
# # listMovieShowDates(cursor, 'The Avengers')
# # listMovieShowTimes(cursor, 'The Avengers')
# listMovieShowHalls(cursor, 'The Avengers')
# listMovieShowDates(cursor, 'The Avengers', 1)
listMovieShowTimes(cursor, 'The Avengers', 1, '2024-05-25')
# getBookedSeats(cursor, 'The Avengers', '2024-05-25', '00:00:00', 4)
# Close the connection
conn.close()
