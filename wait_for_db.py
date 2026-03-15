# wait_for_db.py
import os
import time
import pymysql
import sys
import subprocess

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 3306))
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "MyNewPassword123")
DB_NAME = os.environ.get("DB_NAME", "testdb")

print(f"Waiting for database at {DB_HOST}:{DB_PORT}...")

while True:
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        conn.close()
        print("Database available!")
        break
    except pymysql.err.OperationalError:
        print(f"Database not ready at {DB_HOST}:{DB_PORT}, waiting 3 seconds...")
        time.sleep(3)

# Execute the command passed after the script
if len(sys.argv) > 1:
    subprocess.run(sys.argv[1:])