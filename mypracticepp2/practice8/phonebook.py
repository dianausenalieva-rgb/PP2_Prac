"""
PhoneBook Manager - Python код для работы с функциями и процедурами
"""

import psycopg2
from psycopg2 import sql
from config import DB_CONFIG


class PhoneBookManager:
    """Класс для управления телефонной книгой через функции/процедуры"""
    
    def __init__(self):
        """Инициализация подключения"""
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.conn.autocommit = False
    
    def close(self):
        """Закрытие подключения"""
        if self.conn:
            self.conn.close()
    
    def execute_sql_file(self, filename):
        """Выполнение SQL файла"""
        with open(filename, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        with self.conn.cursor() as cur:
            cur.execute(sql_script)
            self.conn.commit()
            print(f"✅ Выполнен файл: {filename}")
    
    # ==================== 1. ПОИСК ПО ШАБЛОНУ ====================
    
    def search_phonebook(self, pattern):
        """
        Поиск записей по шаблону
        Использует функцию search_phonebook()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
            results = cur.fetchall()
            return results
    
    # ==================== 2. UPSERT ====================
    
    def upsert_user_by_name(self, name, surname, phone):
        """
        Добавление или обновление пользователя
        Использует процедуру upsert_user_by_name()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL upsert_user_by_name(%s, %s, %s);", 
                       (name, surname, phone))
            self.conn.commit()
    
    def upsert_user_by_phone(self, name, surname, phone):
        """
        Добавление или обновление пользователя (версия с ON CONFLICT)
        Использует процедуру upsert_user_by_phone()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL upsert_user_by_phone(%s, %s, %s);", 
                       (name, surname, phone))
            self.conn.commit()
    
    # ==================== 3. МАССОВАЯ ВСТАВКА ====================
    
    def bulk_insert_users(self, users_list):
        """
        Массовая вставка пользователей с валидацией
        users_list: список списков [[name, surname, phone], ...]
        Использует процедуру bulk_insert_users()
        """
        # Преобразуем Python список в PostgreSQL массив
        with self.conn.cursor() as cur:
            # Конвертируем в формат для PostgreSQL
            array_str = '{' + ','.join([
                f'"{name}","{surname}","{phone}"' 
                for name, surname, phone in users_list
            ]) + '}'
            
            cur.execute("CALL bulk_insert_users(%s::text[][]);", (array_str,))
            self.conn.commit()
    
    # ==================== 4. ПАГИНАЦИЯ ====================
    
    def get_paginated_phonebook(self, limit, offset):
        """
        Получение данных с пагинацией
        Использует функцию get_paginated_phonebook()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated_phonebook(%s, %s);", 
                       (limit, offset))
            return cur.fetchall()
    
    def get_paginated_advanced(self, limit, offset, sort_by='name', sort_order='ASC'):
        """
        Получение данных с пагинацией и сортировкой
        Использует функцию get_paginated_phonebook_advanced()
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM get_paginated_phonebook_advanced(%s, %s, %s, %s);
            """, (limit, offset, sort_by, sort_order))
            return cur.fetchall()
    
    # ==================== 5. УДАЛЕНИЕ ====================
    
    def delete_by_name_surname(self, name, surname):
        """
        Удаление по имени и фамилии
        Использует процедуру delete_by_name_surname()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL delete_by_name_surname(%s, %s);", (name, surname))
            self.conn.commit()
    
    def delete_by_phone(self, phone):
        """
        Удаление по телефону
        Использует процедуру delete_by_phone()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL delete_by_phone(%s);", (phone,))
            self.conn.commit()
    
    def delete_user(self, name=None, surname=None, phone=None):
        """
        Универсальное удаление
        Использует процедуру delete_from_phonebook()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL delete_from_phonebook(%s, %s, %s);", 
                       (name, surname, phone))
            self.conn.commit()
    
    # ==================== ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ ====================
    
    def get_all(self):
        """
        Получение всех записей
        Использует функцию get_all_phonebook()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM get_all_phonebook();")
            return cur.fetchall()
    
    def get_statistics(self):
        """
        Получение статистики
        Использует функцию get_phonebook_stats()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM get_phonebook_stats();")
            return cur.fetchone()
    
    def check_user_exists(self, name, surname):
        """
        Проверка существования пользователя
        Использует функцию check_user_exists()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT check_user_exists(%s, %s);", (name, surname))
            return cur.fetchone()[0]
    
    def validate_phone(self, phone):
        """
        Валидация телефона через функцию БД
        Использует функцию validate_phone_format()
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT validate_phone_format(%s);", (phone,))
            return cur.fetchone()[0]
    
    def clear_all(self):
        """
        Очистка всей таблицы
        Использует процедуру clear_all_phonebook()
        """
        with self.conn.cursor() as cur:
            cur.execute("CALL clear_all_phonebook();")
            self.conn.commit()


def print_table(records, headers):
    """Красивый вывод таблицы"""
    if not records:
        print("Нет записей")
        return
    
    # Вывод заголовков
    print("-" * 80)
    for h in headers:
        print(f"{h:<20}", end="")
    print()
    print("-" * 80)
    
    # Вывод данных
    for row in records:
        for col in row:
            print(f"{str(col):<20}", end="")
        print()
    print("-" * 80)


def main():
    """Демонстрация работы"""
    
    print("\n" + "="*80)
    print(" PHONEBOOK MANAGEMENT SYSTEM")
    print("="*80)
    
    # Создаем менеджер
    pb = PhoneBookManager()
    
    try:
        # ========== 1. СОЗДАНИЕ ФУНКЦИЙ И ПРОЦЕДУР ==========
        print("\n1. УСТАНОВКА ФУНКЦИЙ И ПРОЦЕДУР")
        print("-" * 40)
        
        pb.execute_sql_file('functions.sql')
        pb.execute_sql_file('procedures.sql')
        
        # ========== 2. UPSERT ==========
        print("\n2. UPSERT (ВСТАВКА ИЛИ ОБНОВЛЕНИЕ)")
        print("-" * 40)
        
        print("✓ Добавление нового пользователя:")
        pb.upsert_user_by_name("Alice", "Brown", "+15551234567")
        
        print("\n✓ Добавление еще одного:")
        pb.upsert_user_by_name("Bob", "Johnson", "+15559876543")
        
        print("\n✓ Обновление существующего (тот же телефон):")
        pb.upsert_user_by_phone("Robert", "Johnson", "+15559876543")
        
        # ========== 3. ПОИСК ==========
        print("\n3. ПОИСК ПО ШАБЛОНУ")
        print("-" * 40)
        
        print("\n➤ Поиск 'Alice':")
        results = pb.search_phonebook("Alice")
        print_table(results, ["ID", "Name", "Surname", "Phone"])
        
        print("\n➤ Поиск '555':")
        results = pb.search_phonebook("555")
        print_table(results, ["ID", "Name", "Surname", "Phone"])
        
        # ========== 4. МАССОВАЯ ВСТАВКА ==========
        print("\n4. МАССОВАЯ ВСТАВКА С ВАЛИДАЦИЕЙ")
        print("-" * 40)
        
        users = [
            ["Charlie", "Davis", "+15551112222"],
            ["Diana", "Wilson", "invalid_phone"],     # Невалидный
            ["Eve", "Martinez", "+12"],                # Мало цифр
            ["Frank", "Anderson", "+15553334444"],     # Валидный
        ]
        
        print("Вставка 4 пользователей (2 валидных, 2 невалидных):")
        pb.bulk_insert_users(users)
        
        # ========== 5. ПАГИНАЦИЯ ==========
        print("\n5. ПАГИНАЦИЯ")
        print("-" * 40)
        
        print("\n➤ Страница 1 (2 записи):")
        results = pb.get_paginated_phonebook(2, 0)
        print_table(results, ["ID", "Name", "Surname", "Phone"])
        
        print("\n➤ Страница 2 (2 записи):")
        results = pb.get_paginated_phonebook(2, 2)
        print_table(results, ["ID", "Name", "Surname", "Phone"])
        
        # ========== 6. УДАЛЕНИЕ ==========
        print("\n6. УДАЛЕНИЕ")
        print("-" * 40)
        
        print("✓ Удаление по имени и фамилии:")
        pb.delete_by_name_surname("Alice", "Brown")
        
        print("\n✓ Удаление по телефону:")
        pb.delete_by_phone("+15559876543")
        
        # ========== 7. СТАТИСТИКА ==========
        print("\n7. СТАТИСТИКА")
        print("-" * 40)
        
        stats = pb.get_statistics()
        print(f"Всего записей: {stats[0]}")
        print(f"Уникальных телефонов: {stats[1]}")
        print(f"Записей с фамилиями: {stats[2]}")
        
        # ========== 8. ВСЕ ЗАПИСИ ==========
        print("\n8. ВСЕ ЗАПИСИ В ТЕЛЕФОННОЙ КНИГЕ")
        print("-" * 40)
        
        all_records = pb.get_all()
        print_table(all_records, ["ID", "Name", "Surname", "Phone"])
        print(f"\nИтого: {len(all_records)} записей")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        pb.conn.rollback()
    finally:
        pb.close()
    
    print("\n" + "="*80)
    print(" ГОТОВО!")
    print("="*80)


if __name__ == "__main__":
    main()