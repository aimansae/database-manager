import os
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

# created base.html in templates folder
# # run the file typing python3 run.py
