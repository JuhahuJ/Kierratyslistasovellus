from database_connection import get_database_connection


def drop_tables(connection):
    '''remove existing tables'''
    cursor = connection.cursor()
    cursor.execute('''drop table if exists users;''')
    cursor.execute('''drop table if exists recycle;''')
    cursor.execute('''drop table if exists adminpass;''')
    connection.commit()


def create_tables(connection, adminpass):
    '''create needed tables'''
    cursor = connection.cursor()
    cursor.execute(
        '''create table users(id integer primary key, username text, password text);''')
    cursor.execute('''create table adminpass(password text);''')
    cursor.execute(
        '''insert into adminpass (password) values (?)''', (adminpass,))
    cursor.execute('''create table recycle(id integer primary key, username_id integer, bottles_cans integer, cardboard integer,
    electronics integer, glass integer, metal integer, plastic integer, paper integer, batteries integer, clothes integer);''')
    connection.commit()


def initialize_database():
    '''do everything needed for using the app'''
    connection = get_database_connection()
    drop_tables(connection)
    adminpass = input("Give a password for the admin account: ")
    create_tables(connection, adminpass)


if __name__ == "__main__":
    initialize_database()
