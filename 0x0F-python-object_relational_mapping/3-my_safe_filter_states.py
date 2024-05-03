#!/usr/bin/python3
"""
Retrieves and displays all values in the states
where `name` matches the argument provided by the user
from the database `hbtn_0e_0_usa`.
This version of the script is protected against MySQL injections.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    db_connect = db.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s "
        "ORDER BY states.id ASC",
        {'name': argv[4]}
    )

    all_rows = db_cursor.fetchall()

    for row in all_rows:
        print(row)
