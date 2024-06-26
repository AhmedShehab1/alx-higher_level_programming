#!/usr/bin/python3
"""
Script that lists all cities in the db hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY cities.id")

    result_rows = cur.fetchall()

    for row in result_rows:
        print(row)

    cur.close()
    conn.close()
