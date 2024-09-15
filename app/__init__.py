from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import bp
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config')

    app.register_blueprint(bp)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres_db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    print("Conexão ao banco de dados inicializada:", db)

    with app.app_context():
        try:
            with db.engine.connect() as connection:
                result = connection.execute('SELECT 1')
                print("Conexão com o banco de dados estabelecida com sucesso!")
        except OperationalError as e:
            print("Erro ao conectar-se ao banco de dados:", e)

    return app
