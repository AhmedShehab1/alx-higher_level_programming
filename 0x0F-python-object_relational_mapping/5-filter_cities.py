#!/usr/bin/python3
"""
script that takes in state name and displays all cities
in that state (SQL INJECTION FREE)
"""
import sys
import MySQLdb
if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    state_name = sys.argv[4]
    if "'" in state_name:
        state_name.replace("'", "''")
    query = "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id=states.id\
        WHERE states.name=\'{}\' ORDER BY cities.id".format(state_name)
    cur.execute(query)
    result_set = cur.fetchall()
    for city in result_set:
        print(city[0], end=", " if result_set.index(city)
              != len(result_set) - 1 else '\n')
    cur.close()
    conn.close()
