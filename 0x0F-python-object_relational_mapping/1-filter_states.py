#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Lists all states starting with 'N' from the database
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE 'N%' "
             "ORDER BY id ASC")
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
