SELECT first_name, country
    FROM users
 WHERE first_name = '건우' AND country =  '경기도';


SELECT first_name f, country c, age a
    FROM users
WHERE country NOT IN ('경기도', '강원도') 
    AND age BETWEEN 20 AND 30
ORDER BY age;