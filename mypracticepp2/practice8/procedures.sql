--  Добавить
CREATE OR REPLACE PROCEDURE add_contact(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phonebook(first_name, phone)
    VALUES (p_name, p_phone);
END;
$$;


--  Обновить
CREATE OR REPLACE PROCEDURE update_contact(p_id INT, p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook
    SET first_name = p_name,
        phone = p_phone
    WHERE id = p_id;
END;
$$;


--  Удалить
CREATE OR REPLACE PROCEDURE delete_contact(p_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE id = p_id;
END;
$$;