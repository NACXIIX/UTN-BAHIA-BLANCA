from flask import Blueprint, render_template, redirect

bp_main_route = Blueprint("bp_main_route", __name__)

@bp_main_route.route("/", methods = ["POST"])
def PaginaPrincipal():
    return render_template("base.html")