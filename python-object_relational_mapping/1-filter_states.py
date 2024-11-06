#!/usr/bin/python3

import MySQLdb

"""
    Module that fetches all states
    starting with the letter N
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    h = "localhost"
    p = 3306
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    db = MySQLdb.connect(host=h, port=p, user=usr, password=pwd, database=db)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
