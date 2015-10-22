#!flask/bin/python

from App import application
from App import views


application.run(debug=True)
