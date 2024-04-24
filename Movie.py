import pyodbc

class Movie:
    def __init__(self, Name, Description, Genre, EmpId, Cast):
        self.Name = Name
        self.Description = Description
        self.Genre = Genre
        self.EmpId = EmpId
        self.Cast = Cast

def add_movie(movie):
        cursor.execute("EXEC AddMovie ?, ?, ?, ?, ?", movie.Name, movie.Description, movie.Genre, movie.EmpId, movie.Cast)
        conn.commit()

def list_movies():
        cursor.execute("EXEC ListMovies")

        rows = cursor.fetchall()
        for row in rows:
            print("Movie Name:", row.Name)
            print("Description:", row.Description)
            print("Genre:", row.Genre)
            print("Cast Members:", row.Actors)
            print("-" * 50)
    


#---------------------------------------------------------------------------------------------------------------------------#
# Connect to the SQL Server database
conn = pyodbc.connect('Driver={SQL Server};Server={DESKTOP-Q2Q9TUS};Database={Cinema}')
cursor = conn.cursor()

# movie = Movie(Name='The Avengers', Description='Superhero movie', Genre='Action', EmpId=1, Cast='Robert Downey Jr., Chris Evans, Scarlett Johansson')
# add_movie(movie)

list_movies()

# Close the connection
conn.close()