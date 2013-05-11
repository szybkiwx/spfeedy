from application import db, models
import os
import hashlib

salt = os.urandom(16).encode('hex')
pwd = "petrucci0209q"
phash = hashlib.sha256(pwd+salt)


user = models.User(username="andrzej", password=phash.hexdigest(), salt=salt)
db.session.add(user)
db.session.commit()


