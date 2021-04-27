from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''drop table if exists users;''')
    cursor.execute('''drop table if exists recycle;''')
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''create table users(id integer primary key, username text, password text);''')
    cursor.execute('''create table recycle(id integer primary key, username_id integer, bottles_cans integer, cardboard integer, electronics integer, glass integer, metal integer, plastic integer, paper integer, batteries integer, clothes integer);''')
    connection.commit()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()