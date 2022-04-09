
from sqlalchemy import true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class user(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    u_name= db.Column(db.String(50))
    u_contact_no=db.Column(db.Numeric)
    u_address= db.Column(db.String(200))
    u_date_of_birth= db.Column(db.Date)
    u_email= db.Column(db.String(60), unique=True)
    u_passw= db.Column(db.String(30))

