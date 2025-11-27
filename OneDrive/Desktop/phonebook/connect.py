import psycopg2
from config import config

def connect():
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except Exception as e:
        print("Ошибка подключения:", e)
        return None
