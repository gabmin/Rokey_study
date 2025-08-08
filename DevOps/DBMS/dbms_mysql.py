import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

cursor = conn.cursor()

cursor.execute("select DATABASE()")

print(cursor.fetchall())
