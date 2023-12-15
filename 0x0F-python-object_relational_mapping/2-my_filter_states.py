#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa where
name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(state_search)
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
