import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

def auth():
    while True:
        try:
            conn= psycopg2.connect(host=settings.database_hostname, database=settings.database_name, 
                    port=settings.database_port,user=settings.database_username, 
                    password=settings.database_password,cursor_factory=RealDictCursor)
            cursor = conn.cursor()
            print("Database connection is successful")
            break
        except Exception as error:
                print("Connection to database failed")
                print("Error:",error)
                time.sleep(2)
    return cursor,conn
