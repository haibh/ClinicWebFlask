from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

from app import app


@app.route('/')
@app.route('/index')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # return "Hello Boss!  <a href='/logout'>Logout</a>"
        return render_template('index.html', title='Clinic Management', user=session['username'])


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == '1' and request.form['username'] == '1':
        session['logged_in'] = True
        session['username'] = request.form['username']
    else:
        flash('wrong password!')
    return index()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()
