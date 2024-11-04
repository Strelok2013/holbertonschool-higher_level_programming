#!/usr/bin/python3
""" A module that uses MySQLdb
    to fetch all the states in 
    the database 'hbtn_0e_0_usa'
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

    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)

