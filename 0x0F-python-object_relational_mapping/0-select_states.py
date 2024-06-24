#!/usr/bin/python3
"""
Module To List states from hbtn_0e_0_usa db
"""
import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id")

    result_query = cur.fetchall()
    for entity in result_query:
        print(entity)
    cur.close()
    conn.close()
