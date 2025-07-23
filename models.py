from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    age_range = db.Column(db.String(20))
    passport_country = db.Column(db.String(100))
    other_passport_country = db.Column(db.String(100))
    insurance_type = db.Column(db.String(50))
    car_year_range = db.Column(db.String(50))
    medical_type = db.Column(db.String(50))
    vessel_type = db.Column(db.String(50))
    mfo_company_name = db.Column(db.String(100))
    bundle = db.Column(db.String(20))
