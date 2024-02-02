from flask import Flask
from extensions import db,api
from resources import ns
from models import *

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/restxdb'

    db.init_app(app)
    with app.app_context():
        db.create_all()
    api.init_app(app)

    api.add_namespace(ns)
    
    return app


app = create_app()

