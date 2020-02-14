import requests

from config import headers_data


class ApiUser:

    def api_user(self):
        try:
            return requests.get(url="http://182.92.81.159/api/sys/user?page=1&size=1", headers=headers_data)
        except Exception as e:
            print("用户列表请求数据错误{}".format(e))
