# -*- coding: utf-8 -*-

import flask
from models import User
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, DateField, HiddenField, IntegerField, DecimalField, TextAreaField, FileField, validators
from werkzeug import secure_filename

class LoginForm(Form):
    username = TextField("Username", [validators.Length(min=2, max=25)])
    password = PasswordField('Password', [validators.Required()])