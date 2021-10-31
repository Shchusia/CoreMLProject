"""
main api folder
"""
import os

from flask_restplus import Api, fields
from werkzeug import import_string

CONFIG = import_string(os.getenv("APP_SETTINGS", "rest_flask.config.Config"))

API = Api(version=CONFIG.API_VERSION, title=CONFIG.APP_NAME + "_API")

error_model = API.model(
    "ErrorModel",
    {
        "code": fields.Integer(required=True, default=400),
        "title": fields.String(required=True, default=""),
        "detail": fields.String(required=True, default=""),
    },
)
bad_response_model = API.model(
    "BadResponse",
    {
        "status": fields.String(required=True, value="error", default="error"),
        "error": fields.Nested(error_model),
    },
)
