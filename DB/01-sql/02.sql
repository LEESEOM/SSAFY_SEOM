CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
  );

PRAGMA table_info('examples');

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;

ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL;

ALTER TABLE examples
RENAME COLUMN Address TO PostCode;

ALTER TABLE examples
DROP COLUMN PostCode;

SELECT
  *
ORDER BY
  COUNT('성');

