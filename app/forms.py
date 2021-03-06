#!/usr/bin/python
# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, PasswordField, BooleanField, \
    DateTimeField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(u'username', validators=[DataRequired()])
    password = PasswordField(u'password', validators=[DataRequired()])
    remember_me = BooleanField(u'remember_me', default=False)


class PatientForm(FlaskForm):
    patient_id = StringField('patient_id', validators=[DataRequired()])
    patient_name = StringField('patient_name', validators=[DataRequired()])
    patient_phone = StringField('patient_phone', validators=[DataRequired()])
    patient_age = StringField('patient_age', validators=[DataRequired()])
    patient_gender = StringField('patient_gender', validators=[DataRequired()])

    patient_address = StringField('patient_address', validators=[DataRequired()])

    patient_history = TextAreaField('patient_history', validators=[DataRequired()])
    patient_family_history = TextAreaField('patient_family_history', validators=[DataRequired()])

    refresh = SubmitField(u'Làm mới')
    view_all = SubmitField(u'Xem tất cả')
    add_new = SubmitField(u'Thêm mới')
    update = SubmitField(u'Cập nhật')
    delete = SubmitField(u'Xóa bệnh nhân')


class MedicineForm(FlaskForm):
    medicine_id = StringField('medicine_id', validators=[DataRequired()])
    medicine_name = StringField('medicine_name', validators=[DataRequired()])
    medicine_code = StringField('medicine_code', validators=[DataRequired()])
    medicine_group = StringField('medicine_group', validators=[DataRequired()])
    medicine_active_elements = StringField('medicine_active_elements', validators=[DataRequired()])
    medicine_unit = StringField('medicine_unit', validators=[DataRequired()])
    medicine_inventory = StringField('medicine_inventory', validators=[DataRequired()])
    medicine_price = StringField('medicine_price', validators=[DataRequired()])

    refresh = SubmitField(u'Làm mới')
    view_all = SubmitField(u'Xem tất cả')
    add_new = SubmitField(u'Thêm mới')
    update = SubmitField(u'Cập nhật')
    delete = SubmitField(u'Xóa thuốc')


class TreatmentForm(FlaskForm):
    pass


class DiagnosticForm(FlaskForm):
    diagnostic_id = StringField('diagnostic_id', validators=[DataRequired()])
    diagnostic_datetime = DateTimeField('diagnostic_datetime', validators=[DataRequired()])
    diagnostic_bloodpressure = StringField('diagnostic_bloodpressure', validators=[DataRequired()])
    diagnostic_heartbeat = StringField('diagnostic_heartbeat', validators=[DataRequired()])
    diagnostic_temperature = StringField('diagnostic_temperature', validators=[DataRequired()])
    diagnostic_weight = StringField('diagnostic_weight', validators=[DataRequired()])
    diagnostic_bloodtype = StringField('diagnostic_bloodtype', validators=[DataRequired()])
    diagnostic_list = StringField('diagnostic_list', validators=[DataRequired()])

    refresh = SubmitField(u'Làm mới')
    view_all = SubmitField(u'Xem tất cả')
    add_new = SubmitField(u'Thêm mới')
    update = SubmitField(u'Cập nhật')
    delete = SubmitField(u'Xóa')

    patient_id = StringField('patient_id', validators=[DataRequired()])
    get_patient_id = SubmitField(u'Xem thông tin')

