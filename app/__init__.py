# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from flask.ext.ldap import LDAP, login_required

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models