from connect import *

def delete_items():
    
    try:
        
        filmID = input("Enter filmID to delete a record: ")
        db_cursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {filmID}")
        row = db_cursor.fetchone()
        
        if row == None:
            print(f"No record with the filmID {filmID} exists:")

        else:
            db_cursor.execute(f"DELETE FROM tblfilms WHERE filmID = {filmID}")
            db_conn.commit()
            print(f"Record {filmID} deleted.")
        
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")

if __name__ == "__main__":
    delete_items()
            
            
        
