from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://denizard:jwHARoaq5o0krNztdz2ZEcvVjyccpOHa@dpg-crhmhmjv2p9s73bd0u20-a.oregon-postgres.render.com/escola_yxnx'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados

    from routes import alunos  # Importe aqui para evitar importação circular
    app.register_blueprint(alunos)

    return app
