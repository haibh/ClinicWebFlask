#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, g, flash, redirect, render_template, request, session, abort, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, models, login_manager
from .forms import LoginForm, PatientForm, DiagnosticForm, MedicineForm, TreatmentForm

login_manager.login_message = u"Vui lòng đăng nhập"
login_manager.session_protection = "strong"


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    form = PatientForm()
    patients = []

    if form.view_all.data:
        flash('VIEW ALL')
        patients = models.Patient.query.all()

    elif form.add_new.data:
        if form.validate_on_submit():
            flash('ADD NEW')
        else:
            flash(u'Vui lòng điền thông tin')

    return render_template('index.html',
                           form=form,
                           patients=patients)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Query & Login
        user_query = models.User.query.filter_by(username=form.username.data).first()
        if user_query.username == form.username.data and user_query.password == form.password.data:
            flash('Login requested for username="%s",password="%s" remember_me=%s' %
                  (form.username.data, form.password.data, str(form.remember_me.data)))

            login_user(user_query, remember=form.remember_me.data)  # Register to login user
            g.user = user_query

            next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            # if not is_safe_url(next):
            #     return abort(400)
            return redirect(next or url_for('index'))
        else:
            flash("Wrong username/password")

    return render_template('login.html',
                           form=form)


@app.route("/logout")
@login_required
def logout():
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


@app.route('/medicine', methods=['GET', 'POST'])
@login_required
def medicine():
    # return redirect(url_for('medicine'))
    return render_template('medicine.html')


@app.route('/diagnostic', methods=['GET', 'POST'])
@login_required
def diagnostic():
    return render_template('diagnostic.html')


@app.route('/treatment', methods=['GET', 'POST'])
@login_required
def treatment():
    return render_template('treatment.html')
