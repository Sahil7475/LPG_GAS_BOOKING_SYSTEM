
from datetime import timezone
from sqlalchemy import true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class user(db.Model, UserMixin):
    u_id= db.Column(db.Integer, primary_key=True)
    u_name= db.Column(db.String(50))
    u_contact_no=db.Column(db.Numeric)
    u_address= db.Column(db.String(200))
    u_date_of_birth= db.Column(db.Date)
    u_email= db.Column(db.String(60), unique=True)
    u_passw= db.Column(db.String(30))
    bookings = db.relationship('booking', backref="user")
    payments = db.relationship('payment', backref="payment")
    def get_id(self):
        return (self.u_id)

class admin(db.Model):
    admin_id= db.Column(db.Integer, primary_key=True)
    admin_name=db.Column(db.String(50))
    admin_contact_no=db.Column(db.Numeric)
    admin_address=db.Column(db.String(500))
    admin_email=db.Column(db.String(20))
    admin_passw=db.Column(db.String(20))

class booking(db.Model):
    booking_id=db.Column(db.Integer, primary_key=True)
    booking_date_time=db.Column(db.DateTime(timezone=True), default=func.now())
    u_id =db.Column(db.Integer, db.ForeignKey('user.u_id'))
    booking_delivery_date= db.Column(db.Date)
    booking_address=db.Column(db.String(400))
    payments = db.relationship('payment', backref="book")
  


class payment(db.Model):
    payment_id=db.Column(db.Integer, primary_key=True)
    payment_mode=db.Column(db.String(10))
    payment_date_time=db.Column(db.DateTime(timezone=True), default=func.now())
    amount=db.Column(db.Integer)
    u_id =db.Column(db.Integer, db.ForeignKey('user.u_id'))
    booking_id =db.Column(db.Integer, db.ForeignKey('booking.booking_id'))
