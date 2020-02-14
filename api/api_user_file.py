import requests

from config import headers_data


class ApiUserFile:
    def api_user_file(self):
        return requests.post("http://182.92.81.159/api/sys/profile", headers = headers_data)