from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk
import secrets as sct


# Blueprint Configuration
users_bp = Blueprint(
    "users_bp", __name__, 
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/users",
)

@users_bp.route("/debug-try-livestream")
def try_livestream():
    return render_template("try_livestream.html")

@users_bp.route("/debug")
def debug():
    return render_template("dashboard.html")