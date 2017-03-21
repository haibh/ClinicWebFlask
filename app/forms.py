#!/usr/bin/python
# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class PatientForm(FlaskForm):
    patient_name = StringField('patient_name', validators=[DataRequired()])
    patient_phone = StringField('patient_phone', validators=[DataRequired()])
    patient_age = StringField('patient_age', validators=[DataRequired()])
    patient_birth_year = StringField('patient_birth_year', validators=[DataRequired()])
    patient_history = StringField('patient_history', validators=[DataRequired()])
    patient_family_history = StringField('patient_family_history', validators=[DataRequired()])

    view_all = SubmitField(u'Xem tất cả')
    add_new = SubmitField(u'Thêm mới')


class MedicineForm(FlaskForm):
    pass


class TreatmentForm(FlaskForm):
    pass


class DiagnosticForm(FlaskForm):
    pass
