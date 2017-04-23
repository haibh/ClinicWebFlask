#!flask/bin/python
# -*- coding: utf8 -*-

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db, models
import os.path
from datetime import datetime

db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

print("database created")

#################################################################################
user1 = models.User('1', '1')
user2 = models.User('bhh', 'bhh')

patient1 = models.Patient(u'BHH', u'098', u'32', u'nam', u'ở chùa', u'đẹp trai', u'đẹp trai')
patient2 = models.Patient(u'TheMoon', u'0923', u'23', u'nữ', u'vô gia cư', u'đẹp gái', u'đẹp gái')
patient3 = models.Patient(u'TheSun', u'0923', u'23', u'pêđê', u'trên sao hỏa', u'đẹp pêde', u'đẹp pêde')

medicine1 = models.Medicine(u'aspirin', u'mã 1', u'nhóm 1', u'hoạt tính 1', u'hộp', 10, 10000)
medicine2 = models.Medicine(u'toplexin', u'mã 2', u'nhóm 12', u'hoạt tính 2', u'vỉ', 130, 25400)
medicine3 = models.Medicine(u'pracetamon', u'mã 2', u'nhóm 12', u'hoạt tính 2', u'vỉ', 130, 25400)

# diagnostic1 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient1, u'10h')
diagnostic1 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient1, datetime.utcnow())
# diagnostic2 = models.Diagnostic(u'200', u'900', u'36', u'81', u'O', u'bb', patient1, u'10h')
diagnostic2 = models.Diagnostic(u'200', u'900', u'36', u'81', u'O', u'bb', patient1, datetime.utcnow())
# diagnostic3 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient2, u'10h')
diagnostic3 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient2, datetime.utcnow())


treatment1 = models.Treatment(u'khám lần đầu', patient1)
treatment2 = models.Treatment(u'khám lần hai', patient2)

db.session.add(user1)
db.session.add(user2)
db.session.add(patient1)
db.session.add(patient2)
db.session.add(patient3)
db.session.add(medicine1)
db.session.add(medicine2)
db.session.add(medicine3)
db.session.add(diagnostic1)
db.session.add(diagnostic2)
db.session.add(diagnostic3)
db.session.add(treatment1)
db.session.add(treatment2)

db.session.commit()

print (models.User.query.all())
print (models.Patient.query.all())
print (models.Medicine.query.all())
print (models.Treatment.query.all())
print (models.Diagnostic.query.all())

print datetime.utcnow()

