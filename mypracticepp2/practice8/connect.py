"""
Модуль для подключения к PostgreSQL
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG


def get_connection():
    """Создание подключения к базе данных"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None


def test_connection():
    """Тестирование подключения"""
    conn = get_connection()
    if conn:
        print(" Подключение успешно!")
        conn.close()
        return True
    else:
        print(" Ошибка подключения!")
        return False


if __name__ == "__main__":
    test_connection()