#!/usr/bin/python3
"""
Module lists states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        usernm=sys.argv[1],
        passwd=sys.argv[2],
        datab=sys.argv[3]
        )

    cursor = datab.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    mydata = cursor.fetchall()

    for row in mydata:
        print(row)

    cursor.close()
    datab.close()
