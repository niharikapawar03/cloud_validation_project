from utils.api_client import APIClient

class StorageValidator:
    def __init__(self, client: APIClient):
        self.client = client

    def validate_storage(self):
        response, latency = self.client.get("/storage/usage")
        result = {
            "component": "Storage",
            "status_code": response.status_code,
            "latency_ms": latency,
            "result": "PASS" if response.status_code == 200 else "FAIL"
        }
        return result

