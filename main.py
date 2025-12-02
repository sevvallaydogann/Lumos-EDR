"""
Lumos EDR - Main Engine
Scans processes and checks them against VirusTotal Intelligence.
"""
import sys
import os
import time

# Set project root path to handle imports correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# pylint: disable=wrong-import-position
import config
from core.database import DatabaseManager
from core.process_monitor import ProcessMonitor
from core.threat_intel import ThreatIntel

def main():
    """Main execution loop."""
    print("==========================================")
    print("   LUMOS EDR - THREAT HUNTER v1.0")
    print("==========================================\n")

    # 1. Initialize Modules
    print("[-] Initializing modules...")
    db = DatabaseManager()
    monitor = ProcessMonitor()
    intel = ThreatIntel(config.VT_API_KEY)
    
    # 2. Start Scanning
    print("[-] Scanning running processes...")
    processes = monitor.get_running_processes()
    print(f"[+] Found {len(processes)} active processes.\n")

    print("[-] Starting Threat Analysis (VirusTotal)...")
    print("-" * 60)
    print(f"{'PROCESS NAME':<25} {'PID':<10} {'STATUS':<15} {'SCORE'}")
    print("-" * 60)

    # 3. Analysis Loop (Scanning all takes too long, let's check the first 5 for testing)
    # In a real-world scenario, remove [:5] to scan all processes.
    for proc in processes[:5]:
        proc_name = proc['name']
        pid = proc['pid']
        file_hash = proc.get('hash')

        # Skip if hash is missing (likely a system file with restricted access)
        if not file_hash:
            continue

        # Query VirusTotal
        vt_result = intel.check_hash(file_hash)
        
        # Evaluate the result
        status = "UNKNOWN"
        score = "N/A"
        
        if vt_result:
            malicious_count = vt_result.get('malicious', 0)
            total_engines = sum(vt_result.values())
            score = f"{malicious_count}/{total_engines}"
            
            if malicious_count > 0:
                status = "MALICIOUS 🚨"
            else:
                status = "CLEAN ✅"
        else:
            status = "NOT FOUND ❓"

        # Print to console
        print(f"{proc_name:<25} {str(pid):<10} {status:<15} {score}")

        # Log to database
        db.log_scan(proc_name, pid, proc['exe'], status, score)
        
        # Wait a bit to avoid hitting API rate limits (Free tier limitation)
        time.sleep(15) 

    print("-" * 60)
    print("\n[+] Scan Completed. Results saved to database.")

if __name__ == "__main__":
    main()