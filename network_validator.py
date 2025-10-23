from utils.api_client import APIClient

class NetworkValidator:
    def __init__(self, client: APIClient):
        self.client = client

    def validate_network(self):
        response, latency = self.client.get("/network/ping")
        result = {
            "component": "Network",
            "status_code": response.status_code,
            "latency_ms": latency,
            "result": "PASS" if response.status_code == 200 else "FAIL"
        }
        return result

