
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

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

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' +DB_NAME):
        db.create_all(app=app)
        print('created Database!') 