from app import db

class Cashier(db.Model):
    id = db.Column(db.Integer, primery_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    phone_number = db.Column(db.VARCHAR(20), unique=True)
    email = db.Column(db.VARCHAR(50), unique=True)
    password = db.Column(db.VARCHAR(20))




