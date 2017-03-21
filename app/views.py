from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from flask_login import login_user, logout_user, current_user, login_required

from app import app, db, models, login_manager
from .forms import LoginForm
from config import SQLALCHEMY_DATABASE_URI


@app.route('/')
@app.route('/index')
def index():
    if not session.get('logged_in'):
        # return redirect('/login')
        return redirect(url_for('login'))
    else:
        return render_template('index.html',
                               title='Clinic Management',
                               user=session['username'],
                               logged_in=session['logged_in'])


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

            session['logged_in'] = True
            session['username'] = form.username.data

            user_query.authenticated = True
            login_user(user_query, remember=True)  # Register to login user

            return redirect(url_for('index'))
        else:
            flash("Wrong username/password")

    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           user=form.username.data,
                           logged_in=session['logged_in'])


@app.route("/logout")
def logout():
    session['logged_in'] = False

    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()


    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id user to retrieve
    """
    return models.User.query.get(int(id))


@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    return 'NEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
