from flask import Blueprint, render_template

administration_app = Blueprint("administration_app", __name__)


@administration_app.route("/")
def administration():
    return render_template("administration/administration.html")

