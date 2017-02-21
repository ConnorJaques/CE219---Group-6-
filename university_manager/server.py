from config import *
from bottle import *
from entities import *
from pony.orm.integration.bottle_plugin import PonyPlugin
install(PonyPlugin())

'''
    Server module
    =============
    This module provides all the basic functionalities of the application.
    The module is a standard Bottle application and runs on port 8080.
'''

'''
    Index page of the application
'''
@route('/')
def index():
    return template('index')

'''
    Index page for the students section.
    It shows all the students in the system.
'''
@route('/students')
def all_students():
    # select all the students from the db
    students = select(s for s in Student)
    # render the list using the students/index template.
    return template('students/index', students = students)

'''
    Page showing all the info about a student.
'''
@route('/students/<id>/')
def show_student(id):
    # retrieve the student by id from the database
    student = Student[id]
    # render the info using the show template for students
    return template('students/show', student = student)

'''
    Form to edit student information.
'''
@route('/students/<id>/edit')
def edit_student(id):
    # retrieve the student by id from the database
    student = Student[id]
    # render the form using the edit template for students
    return template('students/edit', student = student)

'''
    The method takes in input the edit form for a student and
    update the database accordingly.
'''
@route('/students/<id>/edit', method='POST')
def update_student(id):
    # retrieve the student by id from the database
    student = Student[id]
    # updating the firstname and last name
    student.firstname = request.forms.get('firstname')
    student.lastname = request.forms.get('lastname')

    # redirect the user to the students info page
    redirect("/students/%s/" % id)

'''
    Index page for the courses section.
    It shows all the courses in the system.
'''
@route('/courses')
def all_courses():
    # retrieving all the courses from the db
    courses = select(c for c in Course)
    # render the index page for courses
    return template('courses/index', courses = courses)

'''
    Shows all the info about a course.
'''
@route('/courses/<id>/')
def show_course(id):
    # retrieve the course from the db by id
    course = Course[id]
    # render the info using the show template for course
    return template('courses/show', course = course)

'''
    Form to edit course information.
'''
@route('/courses/<id>/edit')
def edit_course(id):
    # retrieve the course from the db by id
    course = Course[id]
    # render the form using the edit template for course
    return template('courses/edit', course = course)

'''
    The method takes in input the edit form for a course and
    update the database accordingly.
'''
@route('/courses/<id>/edit', method='POST')
def update_course(id):
    # retrieve the course from the db
    course = Course[id]
    # update the course name
    course.name = request.forms.get('name')
    # redirect to the course info page
    redirect("/courses/%s/" % id)

'''
    The method provide a form to a student to a course.
'''
@route('/courses/<id>/add_student')
def add_student_to_course(id):
    # retrieve the course from DB
    course = Course[id]
    # select all the students in the system
    students = select(s for s in Student)
    # render the form using the add_student template
    return template('courses/add_student', course=course, students=students)

'''
    The method takes in input the add_student form for a course and
    update the database accordingly.
'''
@route('/courses/<id>/add_student', method='POST')
def update_student_to_course(id):
    # retrieve the course from the db
    course = Course[id]

    # retrieve the list of students id passed through the form
    students_to_enroll = request.forms.getlist('student')
    # converting them to integers since form values are always strings.
    students_to_enroll = list(map(int,students_to_enroll))

    # loop through the students that has to be enrolled,
    # and add them to the course.
    for sid in students_to_enroll:
        # retrieve the student from the db
        student = Student[sid]
        # if the student is not enrolled yet, add to the enrolled students.
        if student not in course.students:
            course.students.add(student)

    # since the form allows to remove students by unchecking the checkbox,
    # we loop through all the students already enrolled in the course and if it
    # is not in the list passed through the form, we remove them from the course.
    for s in course.students:
        if s.student_id not in students_to_enroll:
            course.students.remove(s)

    redirect("/courses/%s/" % id)

'''
    The method create a form to register an exam for a course.
'''
@route('/courses/<id>/add_exam')
def add_exam_to_course(id):
    # retrieve the course from the db
    course = Course[id]
    return template('courses/add_exam', course=course)

'''
    Add an exam for a student in the course.
'''
@route('/courses/<id>/add_exam', method="POST")
def update_exam_to_course(id):
    # retrieve the course from the db
    course = Course[id]
    # get the student_id of the person who did the exam
    student_id = request.forms.get('student_id')
    # get the mark
    mark = request.forms.get('mark')

    # retrieve the student from the database
    student = Student[student_id]
    # create a new exam object
    exam = Exam(student= student, course=course, mark=mark)
    # add the exam to the course
    course.exams.add(exam)
    # redirect the user to the course info page
    redirect('/courses/%s/' % id)

run(host='localhost', port=8080, debug=True, reloader=True)
