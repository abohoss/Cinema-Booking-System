import pyodbc
from datetime import datetime
class Showtime:
    def __init__(self, Time, Date, MovieName, Hall):
        self.Time = Time
        self.Date = Date
        self.MovieName = MovieName
        self.Hall = Hall

def add_showtime(showtime,cursor):
        cursor.execute("EXEC AddShowTime ?, ?, ?, ?", showtime.Time, showtime.Date, showtime.MovieName, showtime.Hall)
        cursor.commit()

def delete_showtime(Time, Date, MovieName, Hall_no,cursor):
    cursor.execute("Exec deleteShowTime ?, ?, ?, ?", Time, Date, MovieName, Hall_no)
    cursor.commit()



# def convert_date(date_str):
#     # Convert string to datetime object
#     date_obj = datetime.strptime(date_str, '%Y-%m-%d')
#     # Convert datetime object to formatted string
#     formatted_date = date_obj.strftime('%d/%m/%y')
#     return formatted_date

def List_showtimes(cursor):
    cursor.execute("Exec ListShowTimes")
    shows = []
    rows = cursor.fetchall()
    for row in rows:
        shows.append(row)
    return shows




# # Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
# cursor = conn.cursor()

# # Example usage
# showtime = Showtime(Time='20:00', Date='2024-05-01', Movie='The Avengers', Hall=1)
# add_showtime(showtime)


# conn.close()
