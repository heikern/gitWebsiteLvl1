from flask import Flask, render_template, redirect
from App import application
from loginForm import loginForm

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
		print"testing"
		return redirect("/")
	return render_template("login.html",
							lastName = lastName,
							memberStatus = memberStatus,
							hidden = hidden,
							submit = submit)