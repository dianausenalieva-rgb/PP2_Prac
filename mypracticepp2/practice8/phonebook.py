from connect import create_connection

#  Получить все
def get_all():
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_all_contacts()")
    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


#  Поиск
def search(text):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (text,))
    print(cur.fetchall())

    cur.close()
    conn.close()


#  COUNT
def count():
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("SELECT count_contacts()")
    print("Total:", cur.fetchone()[0])

    cur.close()
    conn.close()


#  Добавить
def add(name, phone):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("CALL add_contact(%s, %s)", (name, phone))
    conn.commit()

    cur.close()
    conn.close()


#  Обновить
def update(id, name, phone):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("CALL update_contact(%s, %s, %s)", (id, name, phone))
    conn.commit()

    cur.close()
    conn.close()


#  Удалить
def delete(id):
    conn = create_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (id,))
    conn.commit()

    cur.close()
    conn.close()


#  ТЕСТ
if __name__ == "__main__":
    add("Ali", "1111")
    add("Dana", "2222")

    print("\nALL:")
    get_all()

    print("\nSEARCH:")
    search("Ali")

    print("\nCOUNT:")
    count()

    print("\nUPDATE:")
    update(1, "Ali Updated", "9999")

    print("\nDELETE:")
    delete(2)

    print("\nFINAL:")
    get_all()
