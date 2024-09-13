from flask import Flask
from flask_migrate import Migrate
from db_config import create_app, db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
