from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    if not session.get('logged_in'):
        return redirect('/login')
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
        if form.username.data == '1' and form.password.data == '1':
            flash('Login requested for username="%s",password="%s" remember_me=%s' %
                  (form.username.data, form.password.data, str(form.remember_me.data)))
            session['logged_in'] = True
            session['username'] = form.username.data
            return redirect('/index')
        else:
            flash("Wrong username/password")
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           user=form.username.data,
                           logged_in=session['logged_in'])


    # if form.username.data == '1' and form.password.data == '1':
    #     session['logged_in'] = True
    #     session['username'] = request.form['username']
    #     flash('Login requested for username="%s",password="%s" remember_me=%s' %
    #           (form.username.data, form.password.data, str(form.remember_me.data)))
    # else:
    #     flash('Wrong login')
    # return index()

    # return redirect('/index')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/login')
