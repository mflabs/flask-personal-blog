from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app,db,render_as_batch=True)
    else:
        migrate.init_app(app,db)

from myblog import routes, models


