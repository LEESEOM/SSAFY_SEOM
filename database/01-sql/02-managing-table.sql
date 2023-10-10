PRAGMA foreign_keys = ON;
-- id, title, content
CREATE TABLE article(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    userid INTEGER NOT NULL,
    FOREIGN KEY (userid) REFERENCES user(id)
);

-- 삭제 : DROP
DROP TABLE article;

-- 데이터를 넣는 방법 : INSERT
INSERT INTO article (title, content, userid)
    VALUES ('hi', '이거 들어가네오', 3);

-- ALTER TABLE
ALTER TABLE article ADD COLUMN created_at DATE NOT NULL DEFAULT '';
ALTER TABLE article ADD COLUMN created NOT NULL DEFAULT '';
ALTER TABLE article RENAME COLUMN content TO contents;
ALTER TABLE article DROP column created;

-- 기존 레코드 수정
-- UPDATE
UPDATE article SET created_at = DATE(); 

UPDATE article 
    SET title      = 'update title', 
        content    = 'new content', 
        created_at = '2023-10-09' 
WHERE id = 4;

-- DELETE
DELETE FROM
    article
WHERE
    id = 1;

DELETE FROM
    article
WHERE id IN(
    SELECT id FROM article
    ORDER BY created_at
    LIMIT 2
    );

SELECT *
    FROM article
WHERE id = (
    SELECT id
        FROM article
    ORDER BY id
    LIMIT 1
);

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(30) NOT NULL UNIQUE,
    email varchar(30) UNIQUE
    );

INSERT INTO user (username, email)
    VALUES ('홍길동', 'hong@email.com'),
           ('이순신', 'Yi@email.com'),
           ('이주미', 'Lee@email.com');


-- article 테이블에 userid가 user테이블에
-- 존재하지 않는 경우 삭제
DELETE
    FROM article
WHERE userid NOT IN(
    SELECT id FROM user
    );