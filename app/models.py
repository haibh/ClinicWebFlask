# from sqlalchemy import *
# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
#
# engine = create_engine('sqlite:///tutorial.db', echo=True)
# Base = declarative_base()
#
#
# ########################################################################
# class User(Base):
#     """"""
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#
#     # ----------------------------------------------------------------------
#     def __init__(self, username, password):
#         """"""
#         self.username = username
#         self.password = password
#
#
# # create tables
# Base.metadata.create_all(engine)

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(32), index=True, unique=True)
    patient_phone = db.Column(db.String(32), index=True, unique=True)
    patient_age = db.Column(db.String(32), index=True, unique=True)
    patient_birth_year = db.Column(db.String(32), index=True, unique=True)
    patient_history = db.Column(db.String(32), index=True, unique=True)
    patient_family_history = db.Column(db.String(32), index=True, unique=True)
    patient_description = db.Column(db.String(32), index=True, unique=True)
    patient_diagnostic = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.patient_name)


class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicine_name = db.Column(db.String(32), index=True, unique=True)
    medicine_code = db.Column(db.String(32), index=True, unique=True)
    medicine_group = db.Column(db.String(32), index=True, unique=True)
    medicine_active_element = db.Column(db.String(32), index=True, unique=True)
    medicine_unit = db.Column(db.String(32), index=True, unique=True)
    medicine_inventory = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.medicine_name)


class Diagnostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnostic_name = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.diagnostic_name)


class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treatment_name = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.treatment_name)
