from flask_migrate import upgrade
from db_config import create_app, db

app = create_app()
with app.app_context():
    upgrade()  # Executa as migrações do banco de dados