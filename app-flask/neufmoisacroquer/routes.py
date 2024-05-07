from flask import render_template
from neufmoisacroquer import app

# Controllers
from neufmoisacroquer.controllers.searchcontroller import search_controller

app.register_blueprint(search_controller, url_prefix="/search")

# Default route
@app.route("/")
def index():
    return render_template('index.html')
