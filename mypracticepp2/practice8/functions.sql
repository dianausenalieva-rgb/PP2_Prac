--  Получить все контакты
CREATE OR REPLACE FUNCTION get_all_contacts()
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT id, first_name, phone FROM phonebook ORDER BY id;
END;
$$ LANGUAGE plpgsql;


--  Поиск
CREATE OR REPLACE FUNCTION search_contacts(txt TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, first_name, phone FROM phonebook
    WHERE first_name ILIKE '%' || txt || '%'
       OR phone LIKE '%' || txt || '%';
END;
$$ LANGUAGE plpgsql;


--  COUNT
CREATE OR REPLACE FUNCTION count_contacts()
RETURNS INT AS $$
DECLARE total INT;
BEGIN
    SELECT COUNT(*) INTO total FROM phonebook;
    RETURN total;
END;
$$ LANGUAGE plpgsql;