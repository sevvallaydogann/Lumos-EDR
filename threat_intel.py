"""
Threat Intelligence Module.
"""
import time
import requests

class ThreatIntel:
    """
    Interacts with VirusTotal API to check file reputation.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3/files"
        self.headers = {"x-apikey": self.api_key}

    # pylint: disable=too-many-return-statements
    def check_hash(self, file_hash):
        """
        Checks file hash against VirusTotal database.
        """
        if not file_hash or file_hash == "N/A":
            return None

        url = f"{self.base_url}/{file_hash}"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            return self._handle_response(response)
        except requests.exceptions.RequestException as error:
            print(f"[!] Connection Error: {error}")
            return None

    def _handle_response(self, response):
        """
        Helper method to handle API response codes.
        """
        if response.status_code == 200:
            data = response.json()
            return data['data']['attributes']['last_analysis_stats']
        
        if response.status_code == 404:
            return {"malicious": 0, "undetected": 0, "status": "Not Found"}
            
        if response.status_code == 429:
            print("[!] Warning: API Quota Exceeded. Waiting...")
            time.sleep(15)
            return None
            
        if response.status_code == 401:
            print("[!] Error: Invalid API Key.")
            return None

        print(f"[!] Unexpected Error: {response.status_code}")
        return None