import sqlite3
import psycopg2
pip install psycopg2-binary
dbname = 'iztjchnv'
user = 'iztjchnv'
password = ''
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_conn

pg_curs = pg_conn.cursor()


!wget https: // github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw = true

!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


get_charecters = 'SELECT * FROM charactercreator_character;'
charecters = sl_curs.execute(get_charecters).fetchall()

sl_curs.execute('PRAGMA table_info (charactercreator_character);').fetchall()


create_character_table = """
CREATE TABLE charactercreator_character (
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""


pg_curs = pg_conn.cursor()
pg_curs.execute(create_character_table)
pg_conn.commit()


show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()


for character in characters:
    insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)


pg_conn.commit()
