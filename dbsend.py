import psycopg2
from psycopg2 import sql

db_config = {
    "dbname": "sensor_data",
    "user": "postgres",
    "password": "******",
    "host": "34.46.4.66",
    "port": "5432",
    "sslmode": "require",
    "sslcert": "./client-cert.pem",
    "sslkey": "./client-key.pem",
    "sslrootcert": "server-ca.pem"
}

# Connect to the database
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    print("Connection to remote database established.")
except Exception as e:
    print("Connection failed:", e)