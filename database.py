"""
Core database module for Lumos EDR.
Handles SQLite connections and log storage.
"""
import sqlite3
import datetime

class DatabaseManager:
    """
    Manages the SQLite database for storing scan results.
    """
    def __init__(self, db_name="lumos_logs.db"):
        """Initialize the database connection and create tables."""
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the necessary tables if they do not exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                process_name TEXT,
                pid INTEGER,
                exe_path TEXT,
                status TEXT,
                vt_score TEXT
            )
        """)
        self.conn.commit()

    # pylint: disable=too-many-arguments
    def log_scan(self, process_name, pid, exe_path, status="Unknown", vt_score="N/A"):
        """
        Logs a single scan result to the database.
        Arguments are stored directly into the scan_results table.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO scan_results (timestamp, process_name, pid, exe_path, status, vt_score)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (timestamp, process_name, pid, exe_path, status, vt_score))
        self.conn.commit()

    def get_all_logs(self):
        """Retrieves all logs from the database sorted by latest."""
        self.cursor.execute("SELECT * FROM scan_results ORDER BY id DESC")
        return self.cursor.fetchall()
