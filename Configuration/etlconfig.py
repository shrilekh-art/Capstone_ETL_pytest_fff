import os
from pathlib import Path
from dotenv import load_dotenv

# .env is at project root, two levels up from this file (Configuration/etlconfig.py)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Oracle database
ORACLE_USER = os.environ.get("ORACLE_USER")
ORACLE_PASSWORD = os.environ.get("ORACLE_PASSWORD")
ORACLE_HOST = os.environ.get("ORACLE_HOST", "localhost")
ORACLE_PORT = int(os.environ.get("ORACLE_PORT", 1521))
ORACLE_SERVICE = os.environ.get("ORACLE_SERVICE", "FREEPDB1")

# mysql database
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "retaildwh")

# Linux server
hostname = os.environ.get("LINUX_HOSTNAME")
username = os.environ.get("LINUX_USERNAME")
password = os.environ.get("LINUX_PASSWORD")
remote_file_path = os.environ.get("REMOTE_FILE_PATH", "/root/sales_data.csv")
local_file_path = os.environ.get("LOCAL_FILE_PATH", "SourceSystem/sales_data_linux.csv")

# postgre sql
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", 5432))
POSTGRES_DB = os.environ.get("POSTGRES_DB")