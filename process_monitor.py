"""
Core module for monitoring running processes.
"""
import hashlib
import psutil

class ProcessMonitor:
    """
    Monitors active processes and calculates file hashes.
    """
    def __init__(self):
        pass

    def get_running_processes(self):
        """
        Retrieves list of running processes with PIDs and Hashes.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                proc_info = proc.info
                if proc_info['exe']:
                    proc_hash = self.get_file_hash(proc_info['exe'])
                    proc_info['hash'] = proc_hash
                    processes.append(proc_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        return processes

    def get_file_hash(self, filepath):
        """
        Calculates MD5 hash of a file.
        """
        try:
            with open(filepath, "rb") as file_handle:
                file_hash = hashlib.md5()
                while chunk := file_handle.read(8192):
                    file_hash.update(chunk)
            return file_hash.hexdigest()
        except (OSError, ValueError):
            return None
         