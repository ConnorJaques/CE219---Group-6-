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

#######################################################
### Begin route declaration
#######################################################



#######################################################
### END route declaration
#######################################################

run(host='localhost', port=8080, debug=True, reloader=True)
