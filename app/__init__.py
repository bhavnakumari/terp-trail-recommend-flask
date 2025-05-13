from flask import Flask
from .routes import rec

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rec)
    return app