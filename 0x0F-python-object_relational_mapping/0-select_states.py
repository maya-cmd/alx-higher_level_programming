#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv


def main():
    """
    The main function
    """
    # First connect to the database
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    # Create a cursor object to aid in execution
    db_cursor = db_connect.cursor()
    # Using the cursor execute query
    db_cursor.execute("SELECT * FROM states")
    # Fetch all rows selected from the query
    all_rows = db_cursor.fetchall()
    # Output each row from all the rows selected
    for row in all_rows:
        print(row)


if __name__ == '__main__':
    main()
