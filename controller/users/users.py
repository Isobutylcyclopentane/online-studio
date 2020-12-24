from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk
import secrets as sct


# Blueprint Configuration
users_bp = Blueprint(
    "users_bp", __name__, 
    template_folder="templates",
    static_folder="static"
)

