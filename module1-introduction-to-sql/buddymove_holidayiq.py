#!/usr/bin/env python


import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


# How many total Characters? Table: charactercreator_character
count_characters = 'SELECT COUNT(*) FROM charactercreator_character;'
print('There are ',curs.execute(count_characters).fetchall(), ' total charecters')


# How many of each specific subclass?
cleric = 'SELECT COUNT(*) FROM charactercreator_cleric;'
print('There are ',curs.execute(cleric).fetchall(), ' total clerics')

fighter = 'SELECT COUNT(*) FROM charactercreator_fighter;'
print('There are ',curs.execute(fighter).fetchall(), ' total fighter')

mage = 'SELECT COUNT(*) FROM charactercreator_mage;'
print('There are ',curs.execute(mage).fetchall(), ' total mages')

thief = 'SELECT COUNT(*) FROM charactercreator_thief;'
print('There are ',curs.execute(thief).fetchall(), ' total thief')

necro = 'SELECT COUNT(*) FROM charactercreator_necromancer;'
print('There are ',curs.execute(necro).fetchall(), ' total necromancers, even thought this is the only sub class. the others are just classes')


# How many total Items?
items = 'SELECT COUNT(*) FROM armory_item;'
print('There are ',curs.execute(items).fetchall(), ' total items')


# How many of the Items are weapons? How many are not?
weapon = 'SELECT COUNT(*) FROM armory_weapon;'
print('There are ',curs.execute(weapon).fetchall(), ' total weapons')

non_wep = 174 - 37
print('There are ',non_wep, ' total non-weapons')


# Part 2
import pandas as pd
df = pd.read_csv (r'buddymove_holidayiq.csv')
import sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
c = conn.cursor()
c.execute('CREATE TABLE Holiday (Id, Sports, Religious, Nature, Theatre, Shopping, Picnic)')
conn.commit()
df.to_sql('Holiday', conn, if_exists='replace', index = False)


holiday = 'SELECT COUNT(*) FROM Holiday;'
print('There are ',c.execute(holiday).fetchall(), ' total rows in holiday')

users = 'SELECT COUNT(*) FROM Holiday WHERE Nature >= 100 AND Shopping > 100;'
print('There are ',c.execute(users).fetchall(), ' users who reviewed > 100 Nature and Shopping')