import sqlite3
from sqlite3 import Error

def db_handler():
    # CONNECT DB
    try:
        con = sqlite3.connect("player.db")
        cursor = con.cursor()
    except ConnectionError as e:
        print(f"Experienced an error while connecting to the Database: {e}")
    
    # CREATE TABLE
    try:
        cursor.execute("""
                       CREATE TABLE players (
                       id INTEGER PRIMARY KEY, 
                       name TEXT, 
                       age INTEGER, 
                       score REAL
                       )
                       """)
    except Error as e:
        print(f"Experience an unknown error: {e}")

    # CLOSE CONNECTION
    finally:
        if 'connection' in locals() and con.is_connected():
            cursor.close()
            con.close()
            print("Database connection closed.")
            
    return con

# INSERT DATA INTO TABLE
def insert_data(con, name, age, score):
    try:
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO players (name, age, score) VALUES (?, ?, ?)",
            (name, age, score)
        )
        con.commit()
    # Unsuccessful
    except Error:
        return False

    return

# READ DATA FROM TABLE
def read_name(con):
    try:
        cursor = con.cursor()
        cursor.execute("""
            SELECT name FROM players 
        """)
        return cursor.fetchall()
    except IndexError as e:
        print(f'Unable to grab name from the database players: {e}')

ALLOWED_FILTERS = {"name", "age", "score"}


def get_user_by_filter_factor(con, filter_column, search_value):
    cursor = None
    try:
        if filter_column not in ALLOWED_FILTERS:
            raise ValueError(f"Invalid filter column: {filter_column}")

        cursor = con.cursor()

        sql = f"""
            SELECT *
            FROM players
            WHERE {filter_column} = ? COLLATE NOCASE
        """

        cursor.execute(sql, (search_value,))
        return cursor.fetchall()

    except ValueError as e:
        print(f"Input error: {e}")
        return None

    except sqlite3.Error as e:
        print(f"Database error while querying players: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()

# Structure for future UPDATE logic
def update_db(cur):
    cur.executescript("""
        BEGIN;
        
        COMMIT;
    """)
