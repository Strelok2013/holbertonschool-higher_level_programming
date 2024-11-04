#!/usr/bin/python3
""" A module that uses MySQLdb
    to fetch all the states in 
    the database 'hbtn_0e_0_usa'
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    host = "localhost"
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, username=username, password=password, database=database)
    cur = db.cursor()

    cur.execute("SELECT * FROM %s", database)
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print("%s, " % col)
        print("\n")

