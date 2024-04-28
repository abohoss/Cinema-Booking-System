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
        return cursor.fetchall()
    


#---------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    # # Connect to the SQL Server database
    conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-IG6PNT2};Database={Cinema}')
    cursor = conn.cursor()

    movie = Movie(Name='The Magnificent Seven', Description='Seven gunmen from a variety of backgrounds are brought together by a vengeful young widow to protect her town from the private army of a destructive industrialist.', Genre='Action', EmpId=1, Cast='Denzel Washington, Chris Pratt, Ethan Hawke')
    add_movie(movie, cursor)

    list_movies(cursor)

    # # Close the connection
    conn.close()
