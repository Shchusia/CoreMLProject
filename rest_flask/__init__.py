import os
from logging import Logger

from flask import Blueprint, Flask
from flask_prometheus_metrics import register_metrics
from prometheus_client import make_wsgi_app
from werkzeug import import_string
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from apps import CONFIG, LOGGER, path_to_config

from .api import API
from .api.predict import predict_ns  # noqa
from .utils import bad_response

APP = Flask(CONFIG.SERVICE_NAME)
APP.logger.addHandler(LOGGER)
APP.config.from_object(path_to_config)

BLUEPRINTS = Blueprint(
    CONFIG.SERVICE_NAME + "_API", CONFIG.SERVICE_NAME, url_prefix=CONFIG.BASE_URL
)
API.init_app(BLUEPRINTS)
APP.register_blueprint(BLUEPRINTS)


@APP.errorhandler(404)
def page_not_found(error):
    code = 404
    response = bad_response(
        code=code, title="Method Not Found", detail="404 not found", exc=error
    )
    return response, 404


@APP.errorhandler(502)
def internal_server_error(error):
    code = 502
    response = bad_response(
        code=code,
        title="Internal Server Error",
        detail="Something went wrong on the server",
        exc=error,
    )
    return response, code


# @APP.errorhandler(Exception)
# def logic_error(error):
#     return {"error": 'Web server error', 'msg': str(error)}, 502

register_metrics(APP, app_version="0.0.1", app_config="dev")
dispatcher = DispatcherMiddleware(
    APP.wsgi_app, {CONFIG.BASE_URL + "/metrics": make_wsgi_app()}
)
