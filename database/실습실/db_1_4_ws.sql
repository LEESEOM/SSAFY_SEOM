SELECT first_name f, phone p, country c
    FROM users
WHERE c != '서울'
    AND p LIKE '%-51__-%';