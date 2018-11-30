import pymysql.cursors


def main():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='feng',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            update(connection, cursor)
    finally:
        connection.close()


def insert(connection, cursor):
    # Create a new record
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()


def get(cursor):
    # Read a single record
    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    cursor.execute(sql, ('webmaster@python.org',))
    result = cursor.fetchone()
    print(result)


def update(connection, cursor):
    sql = "UPDATE `users` SET `password` = %s"
    cursor.execute(sql, ('myPwd',))
    connection.commit()


if __name__ == '__main__':
    main()
