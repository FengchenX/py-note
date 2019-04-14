import psycopg2
from service.base import app

# conn  =  psycopg2.connect(database='postgres',user='postgres',password='123456',host='192.168.1.245',port='5432')

class SystemDB(object):
    # def __init__(self):
    #     pass
    def ConnectDB(self):
        self.conn = psycopg2.connect(
            database=app.config['DATABASE'], user=app.config['DBUSER'], password=app.config['DBPWD'], 
            host=app.config['DBHOST'], port=app.config['DBPORT'])
    
    def InitDB(self, file):
        with app.app_context():
            with app.open_resource(file, mode='r') as f:
                self.conn.cursor().execute(f.read())
            self.conn.commit()



# cur = conn.cursor()
# cur.execute("SELECT * FROM testtb LIMIT 10")
# rows = cur.fetchall()
# print(rows)
# conn.commit()
# cur.close()
# conn.close()