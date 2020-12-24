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
    static_folder="static"
)
