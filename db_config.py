from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://denizard:jwHARoaq5o0krNztdz2ZEcvVjyccpOHa@dpg-crhmhmjv2p9s73bd0u20-a.oregon-postgres.render.com/escola_yxnx'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configurações do Swagger
    swagger_config = {
        'title': 'Api Denizard',
        'version': '1.0.0',
        'description': 'Documentação da API para gerenciamento de alunos',
        'terms_of_service': 'http://swagger.io/terms/',
        'contact': {
            'name': 'Suporte',
            'email': 'suporte@exemplo.com'
        },
        'license': {
            'name': 'Licença MIT',
            'url': 'https://opensource.org/licenses/MIT'
        }
    }
    
    swagger = Swagger(app, template=swagger_config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

    from routes import alunos  # Importe aqui para evitar importação circular
    app.register_blueprint(alunos)

    return app
