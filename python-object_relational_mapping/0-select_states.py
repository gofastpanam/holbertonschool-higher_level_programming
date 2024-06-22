#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

db = MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cursor = db.cursor()

cursor.execute("SELECT * FROM states")
results = cursor.fetchall()

for row in results:
    print(row)

db.close()
cursor.close()
