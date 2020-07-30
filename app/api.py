"""
Api and resource binding
"""

from flask import Blueprint
from flask_restful import Api
from routes.send_email import SendEmail


# Create Blueprint:
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)


# Add API Routes:

api.add_resource(SendEmail, '/send', methods=['POST'], endpoint='send_email')
