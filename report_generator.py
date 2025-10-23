import json

def generate_report(results):
    report = {
        "total_tests": len(results),
        "passed": sum(1 for r in results if r["result"] == "PASS"),
        "failed": sum(1 for r in results if r["result"] == "FAIL"),
        "details": results
    }

    with open("validation_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\n✅ Validation Completed. Report saved as validation_report.json")

