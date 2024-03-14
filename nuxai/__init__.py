import requests
import json

from generate import Generate
from index import Index


class NUX:
    def __init__(self, api_key):
        self.base_url = "https://api.nux.ai"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.index = self.Index()
        self.generate = self.Generate()

    def _send_post(self, url, payload):
        request_url = f"{self.base_url}{url}"
        return requests.get(request_url, headers=self.headers, data=payload).json()

    def _send_get(self, url):
        request_url = f"{self.base_url}{url}"
        return requests.get(request_url, headers=self.headers).json()

    def parse(self, modality="text", file_urls=[]):
        parse_url = f"{self.base_url}/parse/{modality}"
        if len(file_urls) == 1:
            data = {"file_urls": file_urls[0]}
        else:
            data = {"file_url": file_urls}
        return self._send_post(parse_url, {"file_urls": file_urls})
