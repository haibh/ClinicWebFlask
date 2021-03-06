from datetime import datetime
from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(32), index=True, unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
            # def get_id(self):
            #     return unicode(self.session_token)

            # def _get_password(self):
            #     return self._password
            #
            #
            # def _set_password(self, password):
            #     self._password = generate_password_hash(password)
            #
            # password = db.synonym('_password',
            #                       descriptor=property(_get_password,
            #                                           _set_password))
            #
            # def check_password(self, password):
            #     if self.password is None:
            #         return False
            #     return check_password_hash(self.password, password)


class Patient(db.Model):
    patient_dic = []
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(32), index=True)
    patient_phone = db.Column(db.String(32), index=True)
    patient_age = db.Column(db.INTEGER, index=True)
    patient_gender = db.Column(db.INTEGER, index=True)
    patient_address = db.Column(db.INTEGER, index=True)
    patient_history = db.Column(db.Text, index=True)
    patient_family_history = db.Column(db.Text, index=True)

    diagnostics = db.relationship('Diagnostic', backref='patient', lazy='dynamic')
    treatments = db.relationship('Treatment', backref='patient', lazy='dynamic')

    def __init__(self, name, phone, age, gender, address, history, familiy_history):
        self.patient_name = name
        self.patient_phone = phone
        self.patient_age = age
        self.patient_gender = gender
        self.patient_address = address
        self.patient_history = history
        self.patient_family_history = familiy_history

    def __repr__(self):
        return '<Patient %r>' % (self.patient_name)


class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # medicine_name = db.Column(db.String(32), index=True, unique=True)
    medicine_name = db.Column(db.String(32), index=True)
    medicine_code = db.Column(db.String(32), index=True)
    medicine_group = db.Column(db.String(32), index=True)
    medicine_active_elements = db.Column(db.Text, index=True)
    medicine_unit = db.Column(db.String(32), index=True)
    medicine_inventory = db.Column(db.INTEGER, index=True)
    medicine_price = db.Column(db.INTEGER, index=True)

    # treatment_id = db.Column(db.INTEGER, db.ForeignKey(Treatment.id))

    def __init__(self, name, code, group, active_elements, unit, inventory, price):
        self.medicine_name = name
        self.medicine_code = code
        self.medicine_group = group
        self.medicine_active_elements = active_elements
        self.medicine_unit = unit
        self.medicine_inventory = inventory
        self.medicine_price = price

    def __repr__(self):
        return '<Medicine %r>' % (self.medicine_name)


class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnostic_name = db.Column(db.String(32), index=True, unique=True)
    diagnostic_bloodpressure = db.Column(db.String(32), index=True)
    diagnostic_heartbeat = db.Column(db.String(32), index=True)
    diagnostic_temperature = db.Column(db.String(32), index=True)
    diagnostic_weight = db.Column(db.String(32), index=True)
    diagnostic_bloodtype = db.Column(db.String(32), index=True)
    diagnostic_list = db.Column(db.String(32), index=True)
    # patient_id = db.Column(db.INTEGER, db.ForeignKey(Patient.id))
    patient_id = db.Column(db.INTEGER, db.ForeignKey('patient.id'))
    # diagnostic_datetime = db.Column(db.String(32), index=True)
    diagnostic_datetime = db.Column(db.DATETIME)

    def __init__(self, bloodpressure, heartbeat, temperature, weight, bloodtype, diagnostic_list, patient,
                 datetime):
        self.diagnostic_bloodpressure = bloodpressure
        self.diagnostic_heartbeat = heartbeat
        self.diagnostic_temperature = temperature
        self.diagnostic_weight = weight
        self.diagnostic_bloodtype = bloodtype
        self.diagnostic_list = diagnostic_list
        self.patient_id = patient.id

        if datetime is None:
            self.diagnostic_datetime = datetime.utcnow()

    def __repr__(self):
        return '<Diagnostic %r>' % (self.id)


class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treatment_name = db.Column(db.String(32), index=True, unique=True)
    treatment_timestamp = db.Column(db.DATETIME, index=True)

    patient_id = db.Column(db.INTEGER, db.ForeignKey(Patient.id))

    # treatment_medicine = db.relationship('Medicine',
    #                                      backref='treatment_medicine', lazy='dynamic')

    def __init__(self, name, timestamp=None):
        self.treatment_name = name
        if timestamp is None:
            self.treatment_timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Treatment %r>' % (self.treatment_name)
