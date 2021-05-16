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

    def find_all(self):
        return self.users

    def create_user(self, user):
        self.users.append(user)
        return user

    def del_user(self, user):
        self.users.pop()


class TestRecycleService(unittest.TestCase):
    def setUp(self):
        self.recycle_service = RecycleService(FakeUserRepository())
        self.user_ahuj = User('ahuj', 'abab223')

    def login(self, user):
        self.recycle_service.register(
            user.username, user.password, user.password)

    def test_add_to_recycle(self):
        self.login(self.user_ahuj)
        asia = Fakesql()
        asia.add_to_bottle_can(3)
        self.assertEqual(asia.recycle_table[2], 3)

    def test_register(self):
        username = self.user_ahuj.username
        password = self.user_ahuj.password
        users = self.recycle_service.get_users()
        self.recycle_service.register(username, password, password)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_del_user(self):
        self.login(self.user_ahuj)
        self.recycle_service.remove_user(self.user_ahuj.username)
        users = self.recycle_service.get_users()
        self.assertEqual(len(users), 0)
