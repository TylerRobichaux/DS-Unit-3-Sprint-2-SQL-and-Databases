#!/usr/bin/env python
# pip install psycopg2-binary
import sqlite3
import psycopg2


# Connecting to elephand data base and making cursor
dbname = 'iztjchnv'
user = 'iztjchnv'
password = 'e6TqKJ1gacDIRLZmhVW_0i1OBNik7JD5'
host = 'ruby.db.elephantsql.com'

conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)
curs = conn.cursor()


# died and survived
query = """
SELECT SUM(survived) FROM titanic
"""
curs.execute(query)
print(curs.fetchall())

query = """
SELECT COUNT(survived) FROM titanic
WHERE survived = 0
"""
curs.execute(query)
print(curs.fetchall())


#How many passengers were in each class
query = """
SELECT SUM(pclass) FROM titanic
GROUP BY pclass
"""
curs.execute(query)
print(curs.fetchall())


# How many died/survived in each class
query = """
SELECT SUM(survived) FROM titanic
GROUP BY pclass
"""
curs.execute(query)
print('survived ',curs.fetchall())


query = """
SELECT COUNT(survived) FROM titanic
WHERE survived = 0
GROUP BY pclass
"""
curs.execute(query)
print('potential zombies ',curs.fetchall())


# Avg ages of survived vs potential zombies
query = """
SELECT AVG(age), pclass FROM titanic
WHERE survived = 0
GROUP BY pclass
"""

query2 = """
SELECT AVG(age), pclass FROM titanic
WHERE survived = 1
GROUP BY pclass
"""

curs.execute(query)
print('Average age of potential zombies ',curs.fetchall())
curs.execute(query2)
print('Average age of survivers ',curs.fetchall())















# Close connection
conn.close()