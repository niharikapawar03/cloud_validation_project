import requests
import time

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        start_time = time.time()
        response = requests.get(f"{self.base_url}{endpoint}")
        latency = round((time.time() - start_time) * 1000, 2)
        return response, latency
