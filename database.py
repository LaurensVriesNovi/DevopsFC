import os
import psycopg2

db_connection = psycopg2.connect(
    database=os.getenv("POSTGRES_DBNAME"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)
