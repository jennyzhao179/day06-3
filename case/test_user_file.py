import unittest

from api.api_user_file import ApiUserFile


class TestUserFile(unittest.TestCase):
    def setUp(self) -> None:
         self.user_file = ApiUserFile()
    def test_user_file(self):
        r = self.user_file.api_user_file()
        str02 = r.json().get("data").get("roles").get("apis")[1]
        mobile = r.json().get("data").get("mobile")

        self.assertEqual("13800000002", mobile)
        self.assertEqual("电饭锅电饭锅", str02)