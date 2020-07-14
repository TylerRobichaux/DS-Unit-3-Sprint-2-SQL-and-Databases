#!/usr/bin/env python
# pip install psycopg2-binary
import pandas as pd
import sqlite3
import psycopg2

# Converting titanic.csv to .sqlite3
df = pd.read_csv (r'titanic.csv')
conn = sqlite3.connect('titanic.sqlite3')
c = conn.cursor()
c.execute('CREATE TABLE titanic (survived, pclass, name, sex, age, siblingsspucesaboard, parentschildrenaboard, fare)')
conn.commit()
df.to_sql('titanic', conn, if_exists='replace', index = False)
get_passengers = 'SELECT * FROM titanic;'
passengers = c.execute(get_passengers).fetchall()

# Connecting to elephand data base and making cursor
dbname = 'iztjchnv'
user = 'iztjchnv'
password = 'e6TqKJ1gacDIRLZmhVW_0i1OBNik7JD5'
host = 'ruby.db.elephantsql.com'

ele_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
ele_curs = ele_conn.cursor()


# Making database to hold titanic data
# classes = "CREATE TYPE pclass_types AS ENUM ('1', '2', '3');"
# sexes = "CREATE TYPE sex_types AS ENUM ('male', 'female');"
# ele_curs.execute(classes)
# ele_curs.execute(sexes)
titanic = """
CREATE TABLE titanic (
  survived INT,
  pclass pclass_types,
  name VARCHAR(80),
  sex sex_types,
  age INT,
  siblingsspucesaboard INT,
  parentschildrenaboard INT,
  
   FLOAT
);
"""

# ele_curs.execute(titanic)
# ele_conn.commit()


# Puting titanc data into the database
get_passengers = 'SELECT * FROM titanic;'
passengers = ele_curs.execute(get_passengers).fetchall()
# print(passengers)
for person in passengers:
  insert_passengers = """
    INSERT INTO titanic
    (survived, pclass, name, sex, age, siblingsspucesaboard, parentschildrenaboard, fare)
    VALUES """ + str(person[1:]) + ";"
  ele_curs.execute(insert_passengers)
  # print(person[1:], '\n')