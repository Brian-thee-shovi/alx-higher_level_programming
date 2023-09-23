#!/usr/bin/python3
"""
script takes an argument and displays all
modules in the state innit
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cur = db.cursor()
    cur.excute("SELECT * FROM states WHERE name
               LIKE BINARY '{}'\ORDER BY states.id ASC".format(sys.argv[4]))

    mydata = cur.fetchall()

    for row in mydata:
        print(row)

    cur.close()
    cur.close()
