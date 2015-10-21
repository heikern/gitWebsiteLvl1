from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class loginForm(Form):
	lastName = StringField('lastName', validators=[DataRequired()])
	memberStatus = BooleanField('memberStatus', default=True)
	submit = SubmitField('submit')