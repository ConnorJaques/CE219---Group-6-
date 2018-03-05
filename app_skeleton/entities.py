import json
import config
from pony.orm import *

'''
The entity module contains all the entities of your application.
We will be using PonyORM; please, refer to http:ponyorm.com for more info.
'''

# instance of the class Database to create and map tables
db = Database()

helllloooooooooo
#######################################################
### Begin entities declaration
#######################################################

class Book(db.Entity):
id = PrimaryKey(int, auto=True)
title = Required(str)
year = Required(int)
author = Required('Author')
publisher = Required('Publisher')
genre = Required('Genre')
order = Required('Order')

class Author(db.Entity):
id = PrimaryKey(int, auto=True)
book = Set(Book)
Firstname = Required(str)
Lastname = Required(str)

class Publisher(db.Entity):
id = PrimaryKey(int, auto=True)
name = Required(str)
country = Required(str)
books = Set(Book)

class Genre(db.Entity):
id = PrimaryKey(int, auto=True)
name = Required(str)
books = Set(Book)

class Customer(db.Entity):
id = PrimaryKey(int, auto=True)
name = Required(str)
lastname = Required(str)
phonenumber = Optional(int)
address = Required(str)
city = Required(str)
country = Required(str)
orders = Set('Order')

class Order(db.Entity):
id = PrimaryKey(int, auto=True)
dop = Required(date)
customer = Required(Customer)
books = Set(Book)

#######################################################
### END entities declaration
#######################################################

#######################################################
### The following 2 instructions bind the db to the
### SQLite file and generate the tables if needed.
#######################################################
# binding the entities to an sqlite database
db.bind('sqlite', config.DB_FILE_NAME, create_db=True)

# create the tables
db.generate_mapping(create_tables=True)
