from neufmoisacroquer import config
from flask import Flask

# Configuration
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

from neufmoisacroquer import routes
