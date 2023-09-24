#!/usr/bin/python3
"""
script takes in the name of a state as an argument then
lists all cities of the state
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
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN\
              states ON state_id = states.id WHERE states.name\
              = %s", (state, ))
    mydata = cur.fetchall()
    cities = ', '.join(city[0] for city in mydata)

    print(cities)
    cur.close()
    db.close()
