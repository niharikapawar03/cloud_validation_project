from utils.api_client import APIClient
from validator.compute_validator import ComputeValidator
from validator.storage_validator import StorageValidator
from validator.network_validator import NetworkValidator
from utils.report_generator import generate_report

BASE_URL = "https://dummyapi.io"  
def main():
    client = APIClient(BASE_URL)

    compute = ComputeValidator(client)
    storage = StorageValidator(client)
    network = NetworkValidator(client)

    results = [
        compute.validate_compute(),
        storage.validate_storage(),
        network.validate_network()
    ]

    for res in results:
        print(f"{res['component']}: {res['result']} ({res['latency_ms']} ms)")

    generate_report(results)

if __name__ == "__main__":
    main()
