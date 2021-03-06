'''this module is responsible for database connection'''
import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    '''returns connection with database'''
    return connection
