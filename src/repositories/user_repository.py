from database_connection import get_database_connection
from entities.user import User


def get_user(row):
    '''returns user if it exists'''
    return User(row['username'], row['password']) if row else None


class UserRepository:
    '''this class is responsible for functions related to users in the database'''
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username):
        '''returns user from database with given username'''
        cursor = self._connection.cursor()
        cursor.execute('select * from users where username = ?', (username,))
        row = cursor.fetchone()
        return get_user(row)

    def find_all(self):
        '''returns all users in database'''
        cursor = self._connection.cursor()
        users = cursor.execute('select * from users').fetchall()
        return users

    def create_user(self, user):
        '''creates user and inserts them into database'''
        cursor = self._connection.cursor()
        cursor.execute('insert into users (username, password) values (?, ?)',
                       (user.username, user.password))
        user_id = cursor.execute(
            'select id from users where username = ?', (user.username,)).fetchone()[0]
        cursor.execute(
            'insert into recycle(username_id, bottles_cans, cardboard, electronics, glass, metal, plastic, paper, batteries, clothes) values (?, 0, 0, 0, 0, 0, 0, 0, 0, 0)', (user_id,))
        self._connection.commit()
        return user

    def check_admin_password(self, password):
        '''gets the admin password from the database'''
        cursor = self._connection.cursor()
        adminpass = cursor.execute('select password from adminpass').fetchone()[0]
        return adminpass

    def del_user(self, username):
        '''deletes a user from the database'''
        cursor = self._connection.cursor()
        cursor.execute('delete from users where username = ?', (username,))
        self._connection.commit()
        return


user_repository = UserRepository(get_database_connection())
