from flask import Flask, render_template, redirect, g, flash, session
from App import application
from loginForm import loginForm
import sqlite3

@application.before_request
def before_request():
	g.db = sqlite3.connect('db1.db')

@application.teardown_request
def teardown_request(exception):
	if hasattr(g,'db'):
		g.db.close()


@application.route('/')
def home():
	return render_template("home.html")

@application.route('/login', methods=["GET", "POST"])
def login():
	lastName = loginForm().lastName
	memberStatus = loginForm().memberStatus
	hidden = loginForm().hidden_tag()
	submit = loginForm().submit
	if loginForm().validate_on_submit():
		userName = lastName.data
		names = g.db.cursor().execute('SELECT name FROM users').fetchall()
		for name in names:
			print name[0]
			print userName
			if name[0] == userName:
				session['logged_in'] = True
				flash('welcome to the club!')
				return render_template("loggedIn.html",
					userName = name[0])
		flash('ehh walao you enter wrong password')
		return redirect("/viewDatabase")
	else:
		flash('please write something in the form')
	return render_template("login.html",
							lastName = lastName,
							memberStatus = memberStatus,
							hidden = hidden,
							submit = submit)

@application.route('/viewDatabase')
def viewDatabase():
	users = g.db.cursor().execute('SELECT * FROM users').fetchall()
	return render_template('viewDatabase.html',
							users = users)

@application.route('/loggedOut')
def loggedOut():
	session.pop("logged_in", None)
	return render_template('loggedOut.html')