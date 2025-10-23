from utils.api_client import APIClient

class ComputeValidator:
    def __init__(self, client: APIClient):
        self.client = client

    def validate_compute(self):
        response, latency = self.client.get("/compute/status")
        result = {
            "component": "Compute",
            "status_code": response.status_code,
            "latency_ms": latency,
            "result": "PASS" if response.status_code == 200 else "FAIL"
        }
        return result
