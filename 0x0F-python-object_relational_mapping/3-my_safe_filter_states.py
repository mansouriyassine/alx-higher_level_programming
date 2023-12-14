#!/usr/bin/python3
import MySQLdb
import sys


def safe_filter_states(username, password, db_name, state_name):
    """
    Display all values in the states table where name matches the argument,
    safe from SQL injection
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )
