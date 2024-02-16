from connect import *

def search_data():
    try:
        
        input_field = input(f"Would you like to search by filmID, title, yearReleased, genre: ")
        if input_field == "filmID":
            id = input("Enter filmID: ")
            db_cursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {id}")
            row = db_cursor.fetchone()
            if row == None:
                print(f"No record with {id} exists in the table: ")

            else:
                for i in row:
                    print(i)
                    
        elif input_field == "title" or input_field == "yearReleased" or input_field == "genre":
            search_input = input(f"Enter search field for {input_field}: ")
            db_cursor.execute(f"SELECT * FROM tblfilms WHERE {input_field} LIKE '%{search_input}%'")
            rows = db_cursor.fetchall()
            if rows == None:
                print(f"No record with field {input_field} Matching '{search_input}' in the table.")
            else:
                for i in rows:
                    print(i)
        else:
            print(f"Invalid search field {input_field}")
    except sql.OperationalError as e:
        print(f"No database or table found: {e}")
if __name__ == "__main__":
    search_data()
            
            
            
    
