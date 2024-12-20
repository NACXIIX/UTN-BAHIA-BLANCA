from flask import Blueprint, request, render_template, redirect, jsonify

bp_login = Blueprint("bp_login", __name__)

@bp_login.route("/")
def PaginaPrincipal():
    return render_template("login.html")

@bp_login.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "user" and password == "123456":
        return redirect("/videojuegos")
    else:
        return render_template("login.html", error="Datos incorrectos")