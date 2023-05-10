from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sqlalchemy import create_engine

db = SQLAlchemy()
DB_NAME = "postgres"


def create_app():
    app = Flask(__name__)
    app.secret_key = "test"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres+psycopg2://admin:admin@localhost:5432/postgres'
    connection_string = 'postgres+psycopg2://admin:admin@localhost:5432/postgres'
    
    db = SQLAlchemy()
    db.init_app(app)
    db=  create_engine(connection_string)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Like

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")
