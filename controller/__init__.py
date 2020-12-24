"""
initializer of the flask app

Author: Jerry Cheng
Last Update 2020.11.19
"""

from flask import Flask


def create_app():
    """Initialize the core application."""
    app = Flask(__name__,
                    instance_path='/instance/config.py', 
                    instance_relative_config=False)

    # application configuration
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Include all Routes
        from controller.auth import auth
        from controller.users import users

        # Register Blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(users.users_bp)
        return app