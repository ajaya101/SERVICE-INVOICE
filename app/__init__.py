from flask import Flask
from app.config import Config
from app.database import init_db
from app.models.invoice import db
from app.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the database
    init_db(app)
    
    # Register the blueprint
    app.register_blueprint(main)
    
    return app
