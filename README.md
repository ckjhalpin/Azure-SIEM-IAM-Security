# Azure SIEM IAM Role Security Scanner 🔐

## 📌 Overview
This script scans **Azure IAM role assignments** for high-risk permissions (`Owner`, `Contributor`) 
and logs them to a SIEM system.  

🚀 **Use case:** **Cloud Security Engineers** can automate security checks and prevent privilege escalation risks.

## ⚙️ How It Works
1. Uses **Azure SDK** to connect to an Azure subscription.
2. Lists **all IAM role assignments**.
3. Flags **high-risk roles** and logs them to a file (`iam_scan_results.log`).
4. Optionally, **integrates with SIEM** (Splunk, Sentinel, Elastic).

## 🏗️ Prerequisites
- **Azure CLI** installed (`az login` required)
- Python 3.x installed
- Install required dependencies:
  ```bash
  pip install azure-identity azure-mgmt-authorization logging

## 🚀 Usage
python3 siem_security_script.py

## 🛠️ Issues & Troubleshooting
1️⃣ ModuleNotFoundError: No module named 'azure.mgmt.authorization'
Install missing package:
pip install azure-mgmt-authorization
2️⃣ InvalidSubscriptionId Error
Ensure you authenticated to Azure using:
az login
3️⃣ No High-Risk Roles Found
Add test role assignments using:
az role assignment create --assignee <user-id> --role "Owner"

## 📜 Sample Log Output

2025-03-11 16:36:09,848 - INFO - 📢 Found role: Owner assigned to 9017f2f9-8430-4a2c-844b-1da51adb2005
2025-03-11 16:36:09,848 - WARNING - ⚠️ HIGH RISK: 9017f2f9-8430-4a2c-844b-1da51adb2005 has Owner role!

## 🔗 Future Enhancements
✅ Send alerts to Microsoft Sentinel
✅ Deploy as Azure Function
✅ Automate role revocation
