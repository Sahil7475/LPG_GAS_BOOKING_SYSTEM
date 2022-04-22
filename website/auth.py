
from logging import error
from flask import Blueprint,render_template, request ,flash, redirect, url_for,Flask
from .models import user
from .models import payment
from .models import booking
from werkzeug.security import generate_password_hash, check_password_hash
from .import db
from datetime import date
from flask_mail import Mail, Message
from flask_login import login_user,login_required,logout_user,current_user
from flask import current_app
import smtplib


auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET' ,'POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        User = user.query.filter_by(u_email=email).first()

        if not User:
            flash('Please sign up before!')

        if User:
                if User.u_passw==password:
                    flash('logged in successfully')
                    login_user(User, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect Password ,try again.', category='error')


    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET' ,'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        contact = request.form.get('contact')
        address = request.form.get('address')
        DOB = request.form.get('DOB')

        User = user.query.filter_by(u_email=email).first()

        if User:
            flash('Email already exists.', category='error')
        elif len(name) < 2:
            flash('name must be greater than 1 characters.', category='error')
        elif len(email) < 3:
            flash('email must be greater than 3 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            entry = user(u_name=name,u_contact_no=contact,u_address=address,u_date_of_birth=DOB,u_email=email, u_passw=password1)
            db.session.add(entry)
            db.session.commit()

            login_user(entry, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html',user=current_user)

    """ u_name u_contact_no u_address u_date_of_birth u_email u_passw """

@auth.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)


@auth.route('/dashboard', methods=["GET","POST"])
def dashboard():
    if request.method == "GET":
        User = user.query.get_or_404(user.u_id)
        login_user(User, remember=True)
    return render_template('dashboard.html', user=current_user)

@auth.route('/admin')
def admin():
    return render_template('admin.html', user=current_user)

@auth.route('/orderhistory', methods=['GET' ,'POST'])
def orderhistory():
    if request.method == "GET":
        User = user
    return render_template('orderhistory.html', user=current_user, book=current_user.bookings)


@auth.route('/payment', methods=['GET' ,'POST'])
def Payment():
    if request.method == 'POST':
        mode = request.form.get('mode')

        cardno = request.form.get('cardno')
        holder = request.form.get('holder')
        month = request.form.get('month')
        year = request.form.get('year')
        book=current_user.u_id

        add=payment(payment_mode=mode,amount=888,u_id=current_user.u_id,booking_id=current_user.u_id)
        db.session.add(add)
        db.session.commit()
        flash("Payment successful", category="success")
        return redirect(url_for('auth.reciept'))


    return render_template('payment.html', user=current_user)

@auth.route('/booking', methods=['GET' ,'POST'])
def Booking():
    if request.method == 'POST':
        address = request.form.get('address')
        date = request.form.get('date')
        email = request.form.get('email')

        message= "Your order is booked"
        server= smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user="sahilj7475@gmail.com",password="Sjadhav@7475")
        server.sendmail(from_addr="sahilj7475@gmail.com", to_addrs=email,msg=message)


        add=booking(u_id=current_user.u_id,booking_delivery_date=date,booking_address=address)
        db.session.add(add)
        db.session.commit()
        flash("Your Order is booked please make a payment", category="success")
        return redirect(url_for('auth.Payment'))

    return render_template('booking.html', user=current_user)


@auth.route('/reciept', methods=['GET' ,'POST'])
def reciept():
    return render_template("reciept.html", user=current_user)
