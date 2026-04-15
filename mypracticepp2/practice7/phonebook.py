import csv
from connect import create_connection

TABLE_NAME = "phonebook"

# Создание таблицы
def create_table():
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print(" Table ready")


#  Добавить контакт
def insert_contact(name, phone):
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    try:
        cur.execute(
            f"INSERT INTO {TABLE_NAME} (first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print(f" Added: {name}")
    except Exception as e:
        print(" Error:", e)
    finally:
        cur.close()
        conn.close()


#  Импорт из CSV (нормальный способ)
def insert_from_csv(filename):
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)

            next(reader, None)  # пропуск заголовка

            count = 0
            for row in reader:
                if len(row) < 3:
                    continue

                name = row[1].strip()
                phone = row[2].strip()

                try:
                    cur.execute(
                        f"INSERT INTO {TABLE_NAME} (first_name, phone) VALUES (%s, %s)",
                        (name, phone)
                    )
                    count += 1
                except Exception as e:
                    print(f"⚠ Skipped {name}: {e}")

            conn.commit()
            print(f" Imported {count} contacts")

    except Exception as e:
        print(" CSV error:", e)

    cur.close()
    conn.close()


#  Поиск
def search_contact(text):
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute(
        f"SELECT * FROM {TABLE_NAME} WHERE first_name ILIKE %s OR phone LIKE %s",
        (f"%{text}%", f"%{text}%")
    )

    rows = cur.fetchall()

    if rows:
        print(f"\n🔍 Found {len(rows)} contact(s):")
        for row in rows:
            print(f"ID:{row[0]} | {row[1]} | {row[2]}")
    else:
        print(" Not found")

    cur.close()
    conn.close()


#  Обновление ПО ID
def update_contact(contact_id, new_name=None, new_phone=None):
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    if new_name:
        cur.execute(
            f"UPDATE {TABLE_NAME} SET first_name=%s WHERE id=%s",
            (new_name, contact_id)
        )

    if new_phone:
        cur.execute(
            f"UPDATE {TABLE_NAME} SET phone=%s WHERE id=%s",
            (new_phone, contact_id)
        )

    conn.commit()
    print(" Updated")

    cur.close()
    conn.close()


#  Удаление ПО ID
def delete_contact(contact_id):
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute(
        f"DELETE FROM {TABLE_NAME} WHERE id=%s",
        (contact_id,)
    )

    print(f"🗑 Deleted: {cur.rowcount}")
    conn.commit()

    cur.close()
    conn.close()


#  Показать все
def show_all():
    conn = create_connection()
    if not conn:
        return
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM {TABLE_NAME} ORDER BY id")
    rows = cur.fetchall()

    if rows:
        print("\n" + "=" * 40)
        print(" ALL CONTACTS")
        print("=" * 40)
        for row in rows:
            print(f"{row[0]}. {row[1]} - {row[2]}")
    else:
        print("📭 Phonebook is empty")

    cur.close()
    conn.close()


#  Меню
def menu():
    create_table()

    while True:
        print("\n" + "=" * 40)
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("7. Exit")
        print("-" * 40)

        choice = input("Choose (1-7): ")

        if choice == '1':
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                insert_contact(name, phone)

        elif choice == '2':
            filename = input("CSV filename (default: data.csv): ").strip()
            if not filename:
                filename = "data.csv"
            insert_from_csv(filename)

        elif choice == '3':
            text = input("Search: ").strip()
            if text:
                search_contact(text)

        elif choice == '4':
            try:
                contact_id = int(input("ID: "))
                new_name = input("New name: ").strip()
                new_phone = input("New phone: ").strip()

                update_contact(
                    contact_id,
                    new_name if new_name else None,
                    new_phone if new_phone else None
                )
            except:
                print(" Invalid ID")

        elif choice == '5':
            try:
                contact_id = int(input("ID to delete: "))
                delete_contact(contact_id)
            except:
                print(" Invalid ID")

        elif choice == '6':
            show_all()

        elif choice == '7':
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice")


if __name__ == "__main__":
    menu()
