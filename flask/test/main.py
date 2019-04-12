import psycopg2
conn = psycopg2.connect(database='postgres',user='postgres',password='123456',host='192.168.1.245',port='5432')
cur = conn.cursor()
cur.execute("SELECT * FROM testtb LIMIT 10")
rows = cur.fetchall()
print(rows)
conn.commit()
cur.close()
conn.close()
