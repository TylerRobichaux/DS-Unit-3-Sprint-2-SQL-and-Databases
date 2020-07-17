# How was working with MongoDB different from working with
# PostgreSQL? What was easier, and what was harder?
# I found working with mongo to be easyer as there are less "rules"
# That being said my minamly educated opinion is that I dont like it as much
# because of the loss rules about data
# I feel if you dont enforce those rules it would be easy to lose data
# not lose in the sence that its done, but in that you dont know where it is


# pipenv install pymongo
# pipenv install dnspython
import sqlite3
import pymongo



# connecting to pymongo
client = pymongo.MongoClient("mongodb+srv://TylerR:@cluster0.0vck6.mongodb.net/<test>?retryWrites=true&w=majority")
db = client.test


# Reading in the charecter db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Sending to pymongo

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()
for character in characters:
    # print(character[2])
    rpg_doc = {
    'doc_type': 'rpg_character',
    'charecter_id': character[0],
    'name': character[1],
    'level': character[2],
    'exp': character[3],
    'hp': character[4],
    'strength': character[5],
    'intellegence': character[6],
    'dexterity': character[7],
    'wisdom': character[8],
    }
    db.test.insert_one(rpg_doc)

