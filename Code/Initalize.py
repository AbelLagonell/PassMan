import pathlib
import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

# Make the directory inside the PassMan
BASE_DIR = (pathlib.Path(__file__) / ".." / ".." ).resolve()
# Making the Passwords directory and the json file if it doesn't exist
pathlib.Path(BASE_DIR / "Passwords").mkdir(parents=True, exist_ok=True)
PASS_DIR = (BASE_DIR / "Passwords").resolve()
db_file = (PASS_DIR / "passwords.db").resolve()
schema_file = (PASS_DIR / "schema.sql").resolve()

#checks if db already exists
if check_db(db_file):
    print('Database already exists. Exiting...')
else:
    #Reads the schema file
    with open(schema_file, 'r') as rf:
        schema = rf.read()

    with sqlite3.connect(db_file) as conn:
        print('Created the connection!')
        # Execute the SQL query to create the table
        conn.executescript(schema)
        print('Created the Table!')
    print('Closed the connection!')

