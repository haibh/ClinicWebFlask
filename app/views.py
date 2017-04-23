#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, g, flash, redirect, render_template, request, session, abort, url_for, jsonify, json
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, models, login_manager
from models import Patient, Medicine, Treatment, Diagnostic
from .forms import LoginForm, PatientForm, DiagnosticForm, MedicineForm, TreatmentForm

login_manager.login_message = u"Vui lòng đăng nhập"
login_manager.session_protection = "strong"
patient_id_session = 0


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    form = PatientForm()
    patients = Patient.query.all()
    #
    # if form.refresh.data:
    #     flash(u'Làm sạch thông tin OK')

    if form.view_all.data:
        patients = Patient.query.all()

    elif form.add_new.data:
        if form.validate_on_submit():
            new_patient = Patient(form.patient_name.data,
                                  form.patient_phone.data,
                                  form.patient_age.data,
                                  form.patient_gender.data,
                                  form.patient_address.data,
                                  form.patient_history.data,
                                  form.patient_family_history.data)
            db.session.add(new_patient)
            db.session.commit()

            # patients = [new_patient]
            flash(u'Thêm mới thành công:' + form.patient_name.data)
        else:
            flash(u"Error: Vui lòng điền thông tin")

    elif form.update.data:
        if form.validate_on_submit():
            updated_patient = models.Patient.query.filter_by(id=int(form.patient_id.data)).first()

            updated_patient.patient_name = form.patient_name.data
            updated_patient.patient_phone = form.patient_phone.data
            updated_patient.patient_age = form.patient_age.data
            updated_patient.patient_gender = form.patient_gender.data
            updated_patient.patient_address = form.patient_address.data
            updated_patient.patient_history = form.patient_history.data
            updated_patient.patient_family_history = form.patient_family_history.data
            db.session.commit()

            # patients = [updated_patient]
            flash(u'Cập nhật thành công: ' + form.patient_name.data)
        else:
            flash(u"Error: Vui lòng điền thông tin")

    elif form.delete.data:
        if form.validate_on_submit():
            delete_patient = models.Patient.query.filter_by(id=int(form.patient_id.data)).first()

            db.session.delete(delete_patient)
            db.session.commit()

            patients = [delete_patient]
            flash(u'Xóa thành công:' + form.patient_name.data)
        else:
            flash(u"Error: Vui lòng điền thông tin")

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
            flash("Error: Wrong username/password")

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
    form = MedicineForm()
    medicines = Medicine.query.all()

    if form.view_all.data:
        medicines = Medicine.query.all()

    elif form.add_new.data:
        if form.validate_on_submit():
            new_medicine = Medicine(form.medicine_name.data,
                                    form.medicine_code.data,
                                    form.medicine_group.data,
                                    form.medicine_active_elements.data,
                                    form.medicine_unit.data,
                                    form.medicine_inventory.data,
                                    form.medicine_price.data)

            db.session.add(new_medicine)
            db.session.commit()

            print new_medicine

            medicines = [new_medicine]
            flash(u'Thêm mới thành công')
        else:
            flash(u"Error: Vui lòng điền thông tin")

    elif form.update.data:
        if form.validate_on_submit():
            updated_medicine = models.Medicine.query.filter_by(id=int(form.medicine_id.data)).first()

            updated_medicine.medicine_name = form.medicine_name.data
            updated_medicine.medicine_code = form.medicine_code.data
            updated_medicine.medicine_group = form.medicine_group.data
            updated_medicine.medicine_active_elements = form.medicine_active_elements.data
            updated_medicine.medicine_unit = form.medicine_unit.data
            updated_medicine.medicine_inventory = form.medicine_inventory.data
            updated_medicine.medicine_price = form.medicine_price.data

            db.session.commit()
            print form.medicine_active_elements.data
            print updated_medicine.medicine_active_elements

            medicines = [updated_medicine]
            flash(u'Cập nhật thành công')
        else:
            flash(u"Error: Vui lòng điền thông tin")

    elif form.delete.data:
        if form.validate_on_submit():
            delete_medicines = models.Medicine.query.filter_by(id=int(form.medicine_id.data)).first()
            print delete_medicines

            db.session.delete(delete_medicines)
            db.session.commit()

            medicines = [delete_medicines]
            flash(u'Xóa thành công')
        else:
            flash(u"Error: Vui lòng điền thông tin")

    return render_template('medicine.html',
                           form=form,
                           medicines=medicines)


@app.route('/diagnostic', methods=['GET', 'POST'])
@login_required
def diagnostic():
    form = DiagnosticForm()

    if form.get_patient_id.data:
        global patient_id_session
        patient_id_session = form.patient_id.data

    current_patient = models.Patient.query.filter_by(id=patient_id_session).first()
    print patient_id_session, current_patient

    if patient_id_session == 0:
        diagnostics = []
    else:
        diagnostics = Diagnostic.query.all()
        # diagnostics = models.Diagnostic.query.filter_by(patient_id=patient_id_session).all()
        # diagnostics = current_patient.diagnostic.all()
    print diagnostics

    return render_template('diagnostic.html',
                           form=form,
                           patient=current_patient,
                           diagnostics=diagnostics,
                           patient_id_session=patient_id_session)


@app.route('/treatment', methods=['GET', 'POST'])
@login_required
def treatment():
    return render_template('treatment.html')


# Get Patient ID by ajax
@app.route('/getId', methods=['POST'])
@login_required
def getId():
    id = request.form['patient_id'];
    user = request.form['patient_name'];
    global patient_id_session
    patient_id_session = int(id)
    return json.dumps({'status': 'OK', 'user': user, 'id': id});
