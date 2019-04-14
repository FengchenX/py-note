
drop table if exists COMPANY;
CREATE TABLE COMPANY
       (ID TEXT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);

drop table if exists entries;
create table entries (
  id integer primary key ,
  title TEXT not null,
  text TEXT not null
);