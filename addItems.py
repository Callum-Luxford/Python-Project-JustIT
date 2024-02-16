from connect import *

def insert_data():
    
    movies = []

    title = input("Enter film Title: ")
    year = input("Enter year of release: ")
    rating = input("enter IMDB Rating: e.g.. ('9.0/10'): ")
    duration = input("Enter film duration: e.g.. ('2h 55m'): ")
    genre = input("Enter film genre: ")
    
    movies.append(title)
    movies.append(year)
    movies.append(rating)
    movies.append(duration)
    movies.append(genre)
    print(f"The film list {movies}")
    
    try:
        
        db_cursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)",(title,year,rating,duration,genre))
        db_conn.commit()
        print(f"title: {title}, Year: {year}, Rating: {rating}, Duration: {duration}, Genre: {genre}, inserted to the table.")
        
    except sql.OperationalError as e:
        db_conn.rollback()
        print(f"Insert failed: {e}")
if __name__ == "__main__":
    insert_data()