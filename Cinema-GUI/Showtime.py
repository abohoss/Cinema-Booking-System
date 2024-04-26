import pyodbc

class Showtime:
    def __init__(self, Time, Date, Movie, Hall):
        self.Time = Time
        self.Date = Date
        self.Movie = Movie
        self.Hall = Hall

def add_showtime(showtime,cursor):
        cursor.execute("EXEC AddShowTime ?, ?, ?, ?", showtime.Time, showtime.Date, showtime.Movie, showtime.Hall)
        cursor.commit()



# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
# cursor = conn.cursor()

# # Example usage
# showtime = Showtime(Time='20:00', Date='2024-05-01', Movie='The Avengers', Hall=1)
# add_showtime(showtime)


# conn.close()