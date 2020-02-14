import unittest

from api.api_login import ApiLogin
from api.api_user import ApiUser
from config import headers_data
from pprint import pprint

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.login = ApiLogin()
    def test_login(self):
        r = self.login.api_login()
        token = "Bearer " + r.json().get("data")
        headers_data["Authorization"]= token
    def test_user(self):
         r = ApiUser().api_user()
         pprint(r.json())
         self.assertEqual(10000, r.json().get("code"))

         self.assertEqual('13800000002', r.json().get("data").get("rows")[0].get("mobile"))



