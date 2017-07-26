#!/usr/bin/python3
"""
5-filter_cities.py - takes in the name of a state as an argument and lists all
 cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    new_list = list()
    search_state = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities "
                "WHERE cities.state_id = "
                "(SELECT states.id "
                "FROM states "
                "WHERE states.name = '{}') "
                "ORDER BY cities.id ASC".format(search_state))
    query_rows = cur.fetchall()
    for row in query_rows:
        new_list.append(row[0])
    print (", ".join(new_list))
    cur.close()
    conn.close()
