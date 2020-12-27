from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk
import secrets as sct
from logics import encrypter

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp", __name__, 
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/auth"
)

LOGIN_NAV_BAR = [{"name":"Forget Password", "url":"/#"}, {"name":"Register", "url":"/register"}]

@auth_bp.route("/")
def homepage():
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    return render_template('login.html', error=error, nav_bar = LOGIN_NAV_BAR)

