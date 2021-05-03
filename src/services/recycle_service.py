from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository)
from database_connection import get_database_connection


class RecycleService:
    '''this class is responsible for the app's functions'''
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        '''logging in a user by finding the user from the database with their username
        and checking if the password given matches the password found in the database'''
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            return print("Wrong username or password")
        self._user = user
        return user

    def register(self, username, password):
        '''creating a user with the given username and password'''
        user = self._user_repository.create_user(User(username, password))
        return user

    def recycle_list(self):
        '''getting the amount of items recycled from the database matching with the current user'''
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        get_recycle = connection.execute(
            'select bottles_cans, cardboard, electronics, glass, metal, plastic, paper, batteries, clothes from recycle where username_id = ?', (username_id,)).fetchone()
        return get_recycle

    def recycle_list_update_bottles_cans(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set bottles_cans = (bottles_cans + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_cardboard(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set cardboard = (cardboard + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_electronics(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set electronics = (electronics + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_glass(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set glass = (glass + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_metal(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set metal = (metal + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_plastic(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set plastic = (plastic + ?) where username_id = ?', 
            (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_paper(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set paper = (paper + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_batteries(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', 
            (username,)).fetchone()[0]
        connection.execute(
            'update recycle set batteries = (batteries + ?) where username_id = ?', (amount, username_id,))
        connection.commit()
        return

    def recycle_list_update_clothes(self, amount):
        connection = get_database_connection()
        username = self._user.username
        username_id = connection.execute(
            'select id from users where username = ?', (username,)).fetchone()[0]
        connection.execute(
            'update recycle set clothes = (clothes + ?) where username_id = ?', (amount, username_id))
        connection.commit()
        return


recycle_service = RecycleService()
