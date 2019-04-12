from db.pg import base

sysDB = base.conn


def CreateTb():
    cur = sysDB.cursor()
    cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
    
    sysDB.commit()
    pass