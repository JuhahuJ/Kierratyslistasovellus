from entities.user import User
from repositories.user_repository import (user_repository as default_user_repository)
from database_connection import get_database_connection


class RecycleService:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            return print("Wrong username or password")
        self._user = user
        return user

    def register(self, username, password):
        user = self._user_repository.create_user(User(username, password))
        return user
        
    def current_user(self):
        user = self._user_repository.find_user(username)
        self._user = user
        return self._user

    def recycle_list(self):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute('select id from users where username = ?', (username,)).fetchone()[0]
        get_recycle = connection.execute('select bottles_cans, cardboard, electronics, glass, metal, plastic, paper, batteries, clothes from recycle where username_id = ?', (username_id,)).fetchone()
        return get_recycle


recycle_service = RecycleService()