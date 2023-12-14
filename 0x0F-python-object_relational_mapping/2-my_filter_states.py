#!/usr/bin/python3
import MySQLdb
import sys


def filter_states_by_input(username, password, db_name, state_name):
    """
    Display all values in the states table where name matches the argument
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_input(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )
