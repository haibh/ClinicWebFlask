#!/usr/bin/python
# -*- coding: utf8 -*-

import datetime
from app import db, models



user1 = models.User('1', '1')
user2 = models.User('bhh', 'bhh')


patient1 = models.Patient(u'BHH', u'098', u'32', u'nam', u'ở chùa', u'đẹp trai', u'đẹp trai')
patient2 = models.Patient(u'TheMoon', u'0923', u'23', u'nữ', u'vô gia cư', u'đẹp gái', u'đẹp gái')
patient3 = models.Patient(u'TheSun', u'0923', u'23', u'pêđê', u'trên sao hỏa', u'đẹp pêde', u'đẹp pêde')

medicine1 = models.Medicine(u'aspirin', u'mã 1', u'nhóm 1', u'hoạt tính 1', u'hộp', 10, 10000)
medicine2 = models.Medicine(u'toplexin', u'mã 2', u'nhóm 12', u'hoạt tính 2', u'vỉ', 130, 25400)
medicine3 = models.Medicine(u'pracetamon', u'mã 2', u'nhóm 12', u'hoạt tính 2', u'vỉ', 130, 25400)

diagnostic1 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient1)
diagnostic2 = models.Diagnostic(u'200', u'900', u'36', u'81', u'O', u'bb', patient1)
diagnostic3 = models.Diagnostic(u'100', u'90', u'36', u'80', u'O', u'aa', patient2)

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
