import unittest
from entities.user import User
from services.recycle_service import RecycleService


class Fakesql:
    def __init__(self, recycle_table=["id", "user_id", 0, 0, 0, 0, 0, 0, 0, 0, 0]):
        self.recycle_table = recycle_table

    def add_to_bottle_can(self, amount):
        self.recycle_table[2] += amount


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_user(self, username):
        matching_users = filter(
            lambda user: user.username == username, self.users)
        matching_users_list = list(matching_users)
        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create_user(self, user):
        self.users.append(user)
        return user


class TestRecycleService(unittest.TestCase):
    def setUp(self):
        self.recycle_service = RecycleService(FakeUserRepository(), Fakesql())
        self.user_ahuj = User('ahuj', 'abab223')

    def login(self, user):
        self.recycle_service.create_user(user.username, user.password)

    def test_add_to_recycle(self):
        self.login_user(self.user_ahuj)
        add_to_bottle_can(3)
        self.assertEqual(recycle_table[2], 3)

    def test_create_user(self):
        username = self.user_ahuj.username
        password = self.user_ahuj.password
        self.recycle_service.create_user(username, password)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)
