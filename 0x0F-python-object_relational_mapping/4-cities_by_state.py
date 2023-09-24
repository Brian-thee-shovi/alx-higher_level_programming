#!/usr/bin/python3
"""
this script lists all cities and module used MySQLdb
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON state_id = states.id")
    mydata = cur.fetchall()
    for row in mydata:
        print(row)

    cur.close()
    db.close()
