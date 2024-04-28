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

# # ---------------------------------------------------------------------------------------------------------------------------#
# Connect to the SQL Server database
# conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
# cursor = conn.cursor()

# movie = Movie(Name='Thor', Description='Superhero movie', Genre='Action', EmpId=1, Cast='Chris Hemsworth, Tom Hiddleston, Natalie Portman, Anthony Hopkins')
# add_movie(movie,cursor)

# list_movies()
# list_movieNames(cursor)
# list_Halls(cursor)
# Close the connection
# conn.close()
