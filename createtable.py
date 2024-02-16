from connect import *

try:
    
    db_cursor.execute("""
        CREATE TABLE "tblfilms" (
            "filmID" INTEGER NOT NULL UNIQUE,
            "title" VARCHAR(50),
            "yearReleased" INTEGER,
            "rating" VARCHAR(50),
            "duration" VARCHAR(20),
            "genre" VARCHAR(50),
            PRIMARY KEY ("filmID" AUTOINCREMENT)
        )""")
    
    print("Table Successfully Created.")
except sql.OperationalError as e:
    print(e)
    