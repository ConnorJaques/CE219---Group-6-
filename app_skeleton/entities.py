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
