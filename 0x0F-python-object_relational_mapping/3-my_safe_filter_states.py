#!/usr/bin/python3
"""
3-my_safe_filter_states.py - write one that is safe from MySQL injections
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
        print(row)
    cur.close()
    conn.close()
