#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in states table that matches it
"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM states WHERE name = \'{}\' ORDER BY id"
                .format(sys.argv[4]))

    result_rows = cur.fetchall()

    for row in result_rows:
        print(row)

    cur.close()
    conn.close()
