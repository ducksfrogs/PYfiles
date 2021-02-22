import psycopg2

conn_string = "host='localhost' dbname='word_dict' user='postgres' password='yama2376'"
print("Connecting to database \n -> %s" % (conn_string))
conn = psycopg2.connect(conn_string)
cur = conn.cursor()
print("Connected!\n")
cur.execute('CREATE TABLE word_dict.table2 (text1 text, time timestamptz, num1 integer, num2 integer)')


cur.execute('INSERT INTO table1 (text1 , time, num1, num2) VALUES(%s, %s, %s, %s)',('Taro','2000-08-01',42, 1000))
cur.execute('INSERT INTO table1 (text1 , time, num1, num2) VALUES(%s, %s, %s, %s)',('Jiro','2010-08-01',90, 130))

def insert_d(i,key,value):
    cur.execute("INSERT INTO table1 VALUES(%s, %s, %s)", (i,key,value))
    conn.commit()

for i, (v, d) in enumerate(zip(json_load.keys(), json_load.values())):
    insert_d(i,v,d)
