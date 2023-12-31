from flask import Flask

from project.blueprints.main import main as main_bp
from project.blueprints.auth import auth as auth_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = __name__  # TODO: Set to something apt
    app.config["DEBUG"] = True

    # Register blueprints
    registered_blueprints = [main_bp, auth_bp]
    for bp in registered_blueprints:
        app.register_blueprint(bp)

    return app
