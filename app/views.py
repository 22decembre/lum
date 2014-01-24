# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, request, g, session, url_for
from flask.ext.login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, DateField, IntegerField, DecimalField, TextAreaField, FileField
from app import app, lm
from config import LANG, LDAP_HOST, LDAP_BASE, LDAP_ID, DOMAIN, LDAP_USERS, LDAP_GROUPS
from models import User
from forms import LoginForm
from lxml import objectify
import os
from werkzeug.datastructures import FileStorage

### présentation

@app.route('/')
@app.route('/index')


# where to create users and manage them
@app.route('/users')




# where to create groups and manage them
@app.route('/groups')


# where each user can see and manage its settings, and also looks like a profile page (change password, avatar... see groups membership)
# depending on the status of the visitor (whever the person is the user itself, an admin, or a guest...) he can change and see differents things
@app.route('/user/<username>')
def user(username):
	i = User(ident=username)
	return render_template("user.html", user = i)


# where we see the group itself. same thing as the user page.
@app.route('/group/<groupname>')


@app.route("/login", methods=["GET", "POST"])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User(ident=form.username.data, password=form.password.data)
		if user.active is not False:
			login_user(user)
			flash("Logged in successfully.")
			return redirect('/user/'+ user.name)
	return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
	logout_user()
	return redirect(url_for("login"))

@app.before_request
def before_request():
    g.user = current_user
    
@lm.user_loader
def load_user(user_id):
	return User(ident=user_id)