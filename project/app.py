from flask import Flask

from . import assets


def create_app() -> Flask:
    """Create Flask app

    Returns:
        Flask: App object with defined setup
    """
    app = Flask(__name__)

    app.config["SECRET_KEY"] = __name__  # TODO: Set to something apt
    app.config["DEBUG"] = True

    # Register blueprints
    with app.app_context():
        assets.load_blueprints()

    return app
