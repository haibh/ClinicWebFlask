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
    # __bind_key__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(32), index=True)
    patient_phone = db.Column(db.String(32), index=True)
    patient_age = db.Column(db.INTEGER, index=True)
    patient_birth_year = db.Column(db.INTEGER, index=True)
    patient_history = db.Column(db.Text, index=True)
    patient_family_history = db.Column(db.Text, index=True)

    patient_diagnostic = db.relationship('Diagnostic',
                                         backref='patient_diagnostic', lazy='dynamic')
    patient_treatment = db.relationship('Treatment',
                                        backref='patient_treatment', lazy='dynamic')

    def __init__(self, name, phone, age, birthyear, history, familiy_history):
        self.patient_name = name
        self.patient_phone = phone
        self.patient_age = age
        self.patient_birth_year = birthyear
        self.patient_history = history
        self.patient_family_history = familiy_history

    def __repr__(self):
        return '<Patient %r>' % (self.patient_name)


class Medicine(db.Model):
    # __bind_key__ = 'medicine'

    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(32), index=True, unique=True)
    medicine_code = db.Column(db.String(32), index=True)
    medicine_group = db.Column(db.String(32), index=True)
    medicine_active_element = db.Column(db.Text, index=True)
    medicine_unit = db.Column(db.String(32), index=True)
    medicine_inventory = db.Column(db.INTEGER, index=True)
    medicine_price = db.Column(db.INTEGER, index=True)

    # treatment_id = db.Column(db.INTEGER, db.ForeignKey(Treatment.id))

    def __init__(self, name, code, group, active_element, unit, inventory, price):
        self.medicine_name = name
        self.medicine_code = code
        self.medicine_group = group
        self.medicine_active_element = active_element
        self.medicine_unit = unit
        self.medicine_inventory = inventory
        self.medicine_price = price

    def __repr__(self):
        return '<Medicine %r>' % (self.medicine_name)


class Diagnostic(db.Model):
    # __bind_key__ = 'diagnostic'

    id = db.Column(db.Integer, primary_key=True)
    diagnostic_name = db.Column(db.String(32), index=True, unique=True)
    diagnostic_type = db.Column(db.String(32), index=True)
    diagnostic_details = db.Column(db.Text, index=True)
    diagnostic_timestamp = db.Column(db.DATETIME, index=True)

    patient_id = db.Column(db.INTEGER, db.ForeignKey(Patient.id))

    def __init__(self, name, type, details, timestamp=None):
        self.diagnostic_name = name
        self.diagnostic_type = type
        self.diagnostic_details = details
        if timestamp is None:
            self.diagnostic_timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Diagnostic %r>' % (self.diagnostic_name)


class Treatment(db.Model):
    # __bind_key__ = 'treatment'

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
