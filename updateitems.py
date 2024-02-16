from connect import *

def update_items():
    
    try:
        
        filmID = input("Enter the filmID to update a record: ")
        
        db_cursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {filmID}")

        result = db_cursor.fetchone()

        if result == None:
            print(f"No record with filmID {filmID} exists")

        else:
            filmID = input("Enter filmID: ")
            title = input("Enter film Title: ")
            year = input("Enter film year: ")
            rating = input("Enter film rating: e.g.. ('9.0/10'): ")
            duration = input("Enter film duration: e.g.. ('2h 55m'): ")
            genre = input("Enter film genre: ")

            db_cursor.execute(f"UPDATE tblfilms SET title = '{title}', yearReleased = '{year}', rating = '{rating}', duration = '{duration}', genre = '{genre}' WHERE filmID = '{filmID}'")
            db_conn.commit()
            print(f"Records {filmID} Updated in the filmflix table")
    
    except sql.OperationalError as e:
        print(f"Failed to update record: {e}")

if __name__ == "__main__":
    update_items()