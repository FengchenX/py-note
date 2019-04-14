
DROP TABLE IF EXISTS COMPANY;
CREATE TABLE COMPANY
       (ID TEXT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);

DROP TABLE IF EXISTS video;
CREATE TABLE video (
  id CHAR(32) PRIMARY KEY,
  name CHAR(64),
  url CHAR(256),
  "desc" CHAR(256),
  thumb CHAR(256)
);