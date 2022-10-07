from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task
# to make the app running, create a root-level directory of /slash
# https://www.geeksforgeeks.org/flask-app-routing/#:~:text=App%20Routing%20means%20mapping%20the,URLs%20and%20make%20navigation%20simpler.


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # has to match model.py database name
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
