from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    # if not session.get('logged_in'):
    #     return render_template('login.html')
    # else:
    #     return render_template('index.html',
    #                            title='Clinic Management',
    #                            user=session['username'],
    #                            logged_in=session['logged_in'])
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for username="%s",password="%s" remember_me=%s' %
              (form.username.data, form.password.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           logged_in=True,
                           user='TestUser')


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
    return index()
