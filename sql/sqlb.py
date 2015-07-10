import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    connection.execute("INSERT INTO population VALUES('New York City', \
        'NY', 820000)")
    connection.execute("INSERT INTO population VALUES('San Francisco', \
        'CA', 900000)")