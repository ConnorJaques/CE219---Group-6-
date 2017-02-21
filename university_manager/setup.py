import json
import config
from entities import *
'''
    Setup module
    ===========

    The setup module should have all the methods that has to be executed before
    the application is started (i.e. seeding the database).
'''


'''
    Seed the database with information from the json dump file.
    NOTE:   this method is specific to each application, which means you have
            to write your import method for your application.
'''
@db_session
def seed_database(dump_filename):
    # reading the json file
    data = json.load(open(dump_filename, 'r'))

    # going through the list of students
    for record in data['Students']:
        # creating a new student object for each entry
        student = Student(firstname = record['firstname'],
                          lastname = record['lastname'])

    # going through the list of courses
    for record in data['Courses']:
        # creating a new course object for each entry
        student = Course(name = record['name'])

if __name__ == "__main__":
    seed_database(config.DB_DUMP_FILE_NAME)
