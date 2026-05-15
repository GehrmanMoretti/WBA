import os
import requests

class WeiboAPI:
    def __init__(self, access_token):
        self.base_url = "https://api.weibo.com/2"
        self.access_token = access_token

    def get_user_timeline(self, uid, count=5):
        url = f"{self.base_url}/statuses/user_timeline.json"
        params = {"access_token": self.access_token, "uid": uid, "count": count}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post_status(self, text):
        url = f"{self.base_url}/statuses/update.json"
        params = {"access_token": self.access_token, "status": text}
        response = requests.post(url, data=params)
        response.raise_for_status()
        return response.json()