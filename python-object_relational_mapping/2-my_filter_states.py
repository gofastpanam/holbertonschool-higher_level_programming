#!/usr/bin/python3
"""
This module takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
It takes 4 arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. state name searched
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ASC order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Error, enter 'username', 'pass', 'db name', 'state name'.")
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

    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' "
                   "ORDER BY states.id ASC".format(state_name))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
