from flask import Flask, render_template, request, redirect
from views import incomingcall_app, administration_app

import config

from flask_migrate import Migrate
from modals import db, Form_call

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)

app.register_blueprint(incomingcall_app, url_prefix="/incomingcall")
app.register_blueprint(administration_app, url_prefix="/administration")

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("base.html")

@app.route("/", methods=["POST"])
def form_call():

    name = request.form["name"]
    phone = request.form["phone"]
    time = request.form["time"]

    if name and phone and time:
        new_call = Form_call(
            name=name,
            phone=phone,
            time=time
        )

        db.session.add(new_call)
        db.session.commit()

    return redirect("/")








