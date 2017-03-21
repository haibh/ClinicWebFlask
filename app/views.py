#!/usr/bin/python
# -*- coding: utf8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, models, login_manager
from .forms import LoginForm

login_manager.login_message = u"Vui lòng đăng nhập"

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html',
                           title=u'Quản lý phòng mạch')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    session['logged_in'] = False
    if form.validate_on_submit():

        # Query & Login
        user_query = models.User.query.filter_by(username=form.username.data).first()
        if user_query.username == form.username.data and user_query.password == form.password.data:
            flash('Login requested for username="%s",password="%s" remember_me=%s' %
                  (form.username.data, form.password.data, str(form.remember_me.data)))

            login_user(user_query, remember=form.remember_me.data)  # Register to login user
            next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            # if not is_safe_url(next):
            #     return abort(400)
            return redirect(next or url_for('index'))
        else:
            flash("Wrong username/password")

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route("/logout")
@login_required
def logout():
    user = current_user
    logout_user()

    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id user to retrieve
    """
    return models.User.query.get(int(id))
# @login_manager.user_loader
# def load_user(session_token):
#     return models.User.query.filter_by(session_token=session_token).first()


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    return 'NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
