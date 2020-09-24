from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
toolbar = DebugToolbarExtension(app)

from sayhello import views, errors, commands

