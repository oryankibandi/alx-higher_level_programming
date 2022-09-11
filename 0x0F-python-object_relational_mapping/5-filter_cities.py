#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa,
safe from sql injection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE %s "
                "ORDER BY cities.id".
            (sys.argv[4]))

    query_rows = cur.fetchall()

    city_list = ""
    for row in query_rows:
        city_list += row[0] + ", "

    print(city_list[0: -2:])

    cur.close()
    conn.close()
