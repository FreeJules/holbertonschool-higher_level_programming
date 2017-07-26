#!/usr/bin/python3
"""
2-my_filter_states.py - displays all values where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    search_for = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (search_for,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == search_for:
            print(row)
    cur.close()
    conn.close()
