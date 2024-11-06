#!/usr/bin/python3

import MySQLdb

"""
    Module that fetches all cities that
    are in a given state.
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    h = "localhost"
    p = 3306
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    search_name = sys.argv[4]

    db = MySQLdb.connect(host=h, port=p, user=usr, password=pwd, database=db)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM `cities` \
                 INNER JOIN states on cities.state_id = states.id \
                 WHERE states.name = %s\
                 ORDER BY cities.id", (search_name,))
    rows = cur.fetchall()
    count = 0
    for row in rows:
        print(row[1], end=', ')
    print('')
