from flask import Blueprint, render_template
from modals import Form_call

incomingcall_app = Blueprint("incomingcall_app", __name__)


@incomingcall_app.route("/",  methods=["GET"])
def incomingcall_list():
    form_call = Form_call.query.order_by(Form_call.id).all()
    return render_template("incomingcall/incomingcall.html", form_call=form_call)
