import requests
import json

from .generate import Generate


class NUX:
    def __init__(self, api_key):
        self.base_url = "http://localhost:8000"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.generate = Generate()

    def _send_post(self, url, payload):
        return requests.post(url, headers=self.headers, data=json.dumps(payload)).json()

    def _send_get(self, url):
        return requests.get(url, headers=self.headers).json()

    def parse(self, file_urls=[]):
        parse_url = f"{self.base_url}/parse/text"
        if len(file_urls) == 1:
            data = {"file_urls": file_urls[0]}
        else:
            data = {"file_url": file_urls}
        return self._send_post(parse_url, {"file_urls": file_urls})
