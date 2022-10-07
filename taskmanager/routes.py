from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
# to make the app running, create a root-level directory of /slash
# https://www.geeksforgeeks.org/flask-app-routing/#:~:text=App%20Routing%20means%20mapping%20the,URLs%20and%20make%20navigation%20simpler.


@app.route("/")
def home():
    return render_template("tasks.html")
