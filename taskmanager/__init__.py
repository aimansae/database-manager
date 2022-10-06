
import os
from flask import Flask  # capiitalF
from flask_sqlalchemy import SQLAlchemy
# to use the hidden environment variables also after deployment
if os.path.exists("env.py"):
    import env
# always like this, create instance of the imported Flask class
# to initialise flask
app = Flask(__name__)
# https://pythonbasics.org/flask-sqlalchemy/
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# always like this craete instance of SQLAlchemy class
# set it to app instance

db = SQLAlchemy(app)


from taskmanager import routes  # noqa
