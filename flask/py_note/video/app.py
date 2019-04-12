from  service import svc
from db.pg import sys

if __name__ == '__main__':
    cur = sys.sysDB.cursor()
    cur.execute("SELECT * FROM testtb LIMIT 10")
    rows = cur.fetchall()
    print(rows)
    sys.sysDB.commit()
    cur.close()
    sys.sysDB.close()
    
    svc.app.run(host='0.0.0.0')