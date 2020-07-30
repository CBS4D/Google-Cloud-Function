"""Flask App Factory Pattern"""

# Import Modules:

from flask import Flask
from flask_cors import CORS
from schemas import ma


# Create Flask App:

flask_app = Flask(__name__)


def create_app(config):
    """
    app factory function
    """
    flask_app.config.from_object(config)

    CORS(flask_app)
    ma.init_app(flask_app)

    from app.api import api_bp as api_module
    flask_app.register_blueprint(api_module)

    return flask_app
