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
