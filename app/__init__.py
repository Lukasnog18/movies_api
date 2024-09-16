from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/lucas/movies_api/instance/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from . import routes
    routes.init_app(app)

    SWAGGER_URL = '/swagger'
    API_URL = "/swagger/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "API FilmesTop"}
    )
    
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/swagger/swagger.json")
    def specs():
        return send_from_directory(os.path.join(os.getcwd(), "static"), "swagger.json")
    
    return app
    