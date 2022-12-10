from flask import Flask, render_template

# create the app
app = Flask(__name__)

#Controllers
from src.controllers.userController import userContoller
app.register_blueprint(userContoller)

@app.route("/")
def hello_world():
    return render_template("index.html")
