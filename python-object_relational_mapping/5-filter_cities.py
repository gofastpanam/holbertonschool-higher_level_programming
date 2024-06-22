#!/usr/bin/python3
"""
This module takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
It takes 4 arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. state name
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ASC order by cities.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error, enter 'username', 'pass', 'db name', 'state_name'.")
        sys.exit(1)

    # Connect to the MySQL Database
    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    state_name = sys.argv[4]

    # Use parameterized query to prevent SQL injection
    query = "SELECT cities.name FROM cities WHERE BINARY states.name = %s "
    "ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
