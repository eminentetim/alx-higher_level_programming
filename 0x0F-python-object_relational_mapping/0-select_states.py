#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=db_name)
        cusor = db.cursor()
        cusor.execute("select * from states order by id")
        for rows in cusor.fetchall():
            print(rows)
        cusor.close()
        db.close()
