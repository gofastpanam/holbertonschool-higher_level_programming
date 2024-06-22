#!/usr/bin/python3
"""
This module lists all states with a name starting
with 'N' from the database hbtn_0e_0_usa.
It takes 3 arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ASC order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error, please enter 'username', 'pass', 'db name'.")
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

    cursor.execute("SELECT * FROM states WHERE states LIKE 'N%' "
                   "ORDER BY states.id ASC")
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
