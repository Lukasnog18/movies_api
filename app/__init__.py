from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import bp
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados (desabilitado por enquanto)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Registrar o Blueprint das rotas da API
    app.register_blueprint(bp)

    # Configuração do Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = "/swagger/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "API FilmesTop"}
    )

    # Registrar o Blueprint do Swagger
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    # Retornar a aplicação Flask configurada

    @app.route("/swagger/swagger.json")
    def specs():
        return send_from_directory(os.path.join(os.getcwd(), "static"), "swagger.json")
    
    print("Aplicação Flask inicializada com Swagger UI")
    return app


    # TODO: Desabilitando a conexão com o banco por enquanto
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/postgres_db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)
    # print("Conexão ao banco de dados inicializada:", db)

    # with app.app_context():
    #     try:
    #         with db.engine.connect() as connection:
    #             result = connection.execute('SELECT 1')
    #             print("Conexão com o banco de dados estabelecida com sucesso!")
    #     except OperationalError as e:
    #         print("Erro ao conectar-se ao banco de dados:", e)