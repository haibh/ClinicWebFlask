from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///user.db', echo=True)

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    login_form_user = str(request.form['username'])
    login_form_pass = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([login_form_user]), User.password.in_([login_form_pass]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
