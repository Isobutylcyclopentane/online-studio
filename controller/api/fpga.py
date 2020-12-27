from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask import current_app as app
import flask as fk
import secrets as sct

# Blueprint Configuration
fpga_bp = Blueprint(
    "fpga_bp", __name__, 
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/auth"
)

@fpga_bp.route("/program-fpga")
def program_fpga():
    return
