import requests


class ApiLogin:
    def __init__(self):
        self.url_login = "http://182.92.81.159/api/sys/login"
    def api_login(self):
        data = {"mobile":"13800000002", "password":"123456"}
        return requests.post(url= self.url_login, json=data)