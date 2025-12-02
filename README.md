# Lumos EDR 

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Security](https://img.shields.io/badge/Security-Blue%20Team-red)
![License](https://img.shields.io/badge/License-MIT-green)

**Lumos EDR** is a lightweight **Endpoint Detection and Response (EDR)** agent designed to monitor system activity, detect suspicious processes, and perform real-time threat analysis using **VirusTotal Intelligence**.

Unlike signature-based antiviruses, Lumos EDR focuses on **Process Hashing** and **Cloud-Based Reputation Checking**, making it an effective tool for identifying zero-day threats or unknown malware.

## Key Features

* **Process Monitoring:** Real-time scanning of active processes and PIDs using `psutil`.
* **Automated Hashing:** Calculates MD5 hashes of running executables on the fly.
* **Threat Intelligence:** Integrates with **VirusTotal API v3** to analyze file reputation.
* **Database Logging:** Stores scan results and incident history in a local SQLite database (`lumos_logs.db`).
* **Modular Architecture:** Built with a scalable structure (`Core`, `Database`, `Intel` modules).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/Lumos-EDR.git](https://github.com/KULLANICI_ADIN/Lumos-EDR.git)
    cd Lumos-EDR
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    * Open `config.py`.
    * Paste your **VirusTotal API Key** into the `VT_API_KEY` variable.
    * *(Get a free key from [VirusTotal](https://www.virustotal.com/))*

## Usage

Run the main engine to start the threat hunting process:

```bash
python main.py
```

## Example Output 

```bash
==========================================
   LUMOS EDR - THREAT HUNTER v1.0
==========================================

[-] Initializing modules...
[-] Scanning running processes...
[+] Found 316 active processes.

[-] Starting Threat Analysis (VirusTotal)...
------------------------------------------------------------
PROCESS NAME              PID        STATUS          SCORE
------------------------------------------------------------
steamwebhelper.exe        464        CLEAN ✅        0/76
unknown_miner.exe         1337       MALICIOUS 🚨    58/76
smss.exe                  824        CLEAN ✅        0/76
------------------------------------------------------------

[+] Scan Completed. Results saved to database.
```

## Project Structure

```bash
Lumos-EDR/
│
├── main.py                 # Main execution engine
├── config.py               # API keys and settings
├── requirements.txt        # Dependencies
│
└── core/                   # Core Modules
    ├── database.py         # SQLite Manager
    ├── process_monitor.py  # System Process Scanner
    └── threat_intel.py     # VirusTotal API Integration
```

## Disclaimer 

This tool is developed for educational and defensive purposes only. The author is not responsible for any misuse. Always test on isolated environments.


