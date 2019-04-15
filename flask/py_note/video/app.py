from  service import svc
from db.pg import sysdb

if __name__ == '__main__':

    # cur = sys.sysDB.cursor()
    # cur.execute("SELECT * FROM testtb LIMIT 10")
    # rows = cur.fetchall()
    # print(rows)
    # sys.sysDB.commit()
    # cur.close()

    videoDB= sysdb.VideoSysDB('/home/f/py-note/flask/py_note/video/db/pg/schema.sql')
    videoDB.ConnectDB()
    # videoDB.InitDB(videoDB.Sql)
    svc.videoDB=videoDB

    svc.app.run(host='0.0.0.0')