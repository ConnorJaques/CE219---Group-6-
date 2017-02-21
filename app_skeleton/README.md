# App Skeleton v0.1

## Development
The 3tier app is made of three 3 files:  

1.  setup.py
2.  entity.py
3.  server.py

The 3tier app also uses three directories:

1. data
2. db
3. views

### Files
#### setup.py file
This file should contain all the methods to initialize your database,
typically by creating the database and loading some dummy data.

#### entities.py file
This file should contain all the entities declaration that you need for
your application.

#### server.py
This file is contains all the bottle routes of your application, which means
all the business logic of the app.

### Directories
#### data
You can put your dummy data here.

#### db
The directory used to store the sqlite database.

#### views
The directory used to store the templates for the app.

## Running the app
To run the app you have to do these 3 steps:

1. Execute the application setup by typing `python setup.py`. You need to do it
  only once, or when you made changes to the database.  
2. Start the bottle application by typing `python server.py`.  
3. Open a browser and go to http://localhost:8080.  
