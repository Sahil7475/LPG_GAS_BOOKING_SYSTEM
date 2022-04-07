from flask import Blueprint,render_template, request ,flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET' ,'POST'])
def login():
    return render_template("login.html")

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

         
        if len(name) < 2:
            flash('name must be greater than 1 characters.', category='error')
        elif len(email) < 3:
            flash('email must be greater than 3 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template('sign_up.html')    