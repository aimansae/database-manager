from taskmanager import db
# no need to import integer float as db already contains it

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # db.String(25 to set the max character)
    # unique=True to make sure it-s unique
    # nullable=Flase to make sure its not empty, reuired
    # repr to represent itself in form of string
    # always like this see link above
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(25), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    # db.Text allows longer string, inputs too
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # to include time too use db.DateTime or db.Time
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
