from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	check_field = BooleanField()
	submit = SubmitField('Отправить в чат')