import datetime
from app import db, models

# CREATE FIRST DATA


user1 = models.User('1', '1')
user2 = models.User('bhh', 'bhh')
db.session.add(user1)
db.session.add(user2)

patient1 = models.Patient('BHH', '098', '32', '1985', 'dep trai', 'dep trai')
patient2 = models.Patient('TheMoon', '0923', '23', '2321', 'dep gai', 'dep gai')
db.session.add(patient1)
db.session.add(patient2)

medicine1 = models.Medicine('aspirin', 'cam', 'haha', 'co gi dau', 'hop', 10, 10000)
medicine2 = models.Medicine('toplexin', 'ho', 'haha', 'co gi adsfasdfdau', 'vi', 130, 25400)
db.session.add(medicine1)
db.session.add(medicine2)

treatment1 = models.Treatment('kham lan dau', None, user1)
treatment1 = models.Treatment('kham lan 2', None, user2)

db.session.commit()

print (models.User.query.all())
print (models.Patient.query.all())
print (models.Medicine.query.all())
print (models.Treatment.query.all())
