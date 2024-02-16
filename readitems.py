from connect import *

def read_items():
    
    try:
        db_cursor.execute("SELECT * FROM tblfilms")
        result = db_cursor.fetchall()
        if not result: 
            print(f"No record(s) exist")
        else:
            for i in result:
                print(i)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")

if __name__ == "__main__":
    read_items()