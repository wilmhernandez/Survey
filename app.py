from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "Let's GO"

debug = DebugToolbarExtension(app)