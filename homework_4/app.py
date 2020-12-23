from flask import Flask, render_template
from views import administration_app

app = Flask(__name__)
app.register_blueprint(administration_app, url_prefix="/administration")

@app.route("/")
def index():
    return render_template("base.html")







