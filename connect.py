# // Import database Module
import sqlite3 as sql

try:
    
    with sql.connect("filmflix.db") as db_conn:
        
        print("Connection established")
        db_cursor = db_conn.cursor()
    
except sql.OperationalError as e:
    print(f"Connection failed, error {e}")
