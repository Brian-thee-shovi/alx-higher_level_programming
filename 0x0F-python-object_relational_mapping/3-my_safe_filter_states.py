#!/usr/bin/python3
"""
module lists all the states table of hbtn_0e_0_usa
where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    state = sys.argv[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s\
              ORDER BY states.id ASC", (state,))
    mydata = c.fetchall()
    for row in mydata:
        print(row)

    c.close()
    db.close()
