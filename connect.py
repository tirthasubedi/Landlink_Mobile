import MySQLdb

def connect():
    conn = MySQLdb.connect(db="cfa", host="localhost", user="cfa", passwd="kKGP4ylKt9n1UJac", port=3306)
    cur = conn.cursor()
    return conn, cur

