CREATE TABLE users(
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phoneNumber NOT NULL,
    gender INTEGER,
    address NOT NULL default 'no address'
    );

ALTER TABLE users
    RENAME COLUMN phoneNumber
        TO number;
 
DROP TABLE users;