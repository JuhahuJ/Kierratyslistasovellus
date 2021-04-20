from database_connection import get_database_connection
from entities.user import User

def get_user(row):
    return User(row['username'], row['password']) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute('select * from users where username = ?', (username,))
        row = cursor.fetchone()
        return get_user(row)

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute('insert into users (username, password) values (?, ?)', (user.username, user.password))
        self._connection.commit()
        return user

user_repository = UserRepository(get_database_connection())