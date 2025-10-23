🚀 Overview

This project automates the validation of core cloud services — Compute, Storage, and Network — using Python and REST APIs.
It performs reliability and performance checks by making API calls, measuring latency, verifying responses, and generating a test report.

The project aligns with Cloud Validation, Automation, and CI/CD Quality Gate practices used in large-scale environments like Krutrim Cloud (Ola AI & Cloud Division).
🧠 Features

✅ Automated validation of cloud service components
✅ REST API-based testing for compute, storage, and network endpoints
✅ Python-based report generation (JSON output)
✅ Modular design for easy extension
✅ Optional CI/CD integration via GitHub Actions

Architecture
Cloud Service Endpoints (mocked via Flask)
        ↓
Python Automation Framework
        ↓
Compute / Storage / Network Validation
        ↓
Latency & Status Analysis
        ↓
JSON Report Generation
        ↓
(Optionally) CI/CD Pipeline Trigger

🗂️ Folder Structure
cloud_validation_project/
│
├── main.py
├── validator/
│   ├── __init__.py
│   ├── compute_validator.py
│   ├── storage_validator.py
│   ├── network_validator.py
│
├── utils/
│   ├── api_client.py
│   ├── report_generator.py
│
├── requirements.txt
└── README.md

