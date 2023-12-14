#!/usr/bin/python3
import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    """
    Lists all cities of a given state
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )
