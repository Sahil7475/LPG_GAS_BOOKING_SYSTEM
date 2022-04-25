from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_mail import Mail
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "data.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] ='LPG booking'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/lpggas'
    
    db.init_app(app)
    
    

    from .views import views
    from .auth import auth
   

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import user
    from .models import payment

    login_manager = LoginManager()
    login_manager.login_view= 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(u_id):
        return user.query.get(int(u_id))



    return app

""" def create_database(app):
    if not path.exists('website/' +DB_NAME):
        db.create_all(app=app)
        print('created Database!')  """