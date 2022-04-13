
from flask import Blueprint,render_template, request ,flash, redirect, url_for
from .models import user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from datetime import date
auth = Blueprint('auth',__name__)




@auth.route('/login', methods=['GET' ,'POST'])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        User = user.query.filter_by(u_email=email).first()
        
        if not User:
            flash('Please sign up before!')
            
        elif User.u_passw==password:
            flash('logged in successfully')
            return render_template('home.html')
          
      
   
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

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
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
       
    return render_template('sign_up.html')  

    """ u_name u_contact_no u_address u_date_of_birth u_email u_passw """

@auth.route('/contact')
def contact():
    return render_template('contact.html') 