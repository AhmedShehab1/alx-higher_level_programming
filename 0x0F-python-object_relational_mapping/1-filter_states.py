#!/usr/bin/python3
"""
script that lists states starting with capital 'N' in hbtn_0e_0_usa db
"""
import sys
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id")
    result_rows = cur.fetchall()
    for row in result_rows:
        print(row)

    cur.close()
    conn.close()
