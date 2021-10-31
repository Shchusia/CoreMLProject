import os

from werkzeug import import_string
from werkzeug.serving import run_simple

from rest_flask import dispatcher
from rest_flask.utils import parser

# from rest_flask.app import APP

if __name__ == "__main__":
    args = parser.parse_args()
    path_to_config = os.getenv("APP_SETTINGS", "rest_flask.config.Config")
    CONFIG = import_string(path_to_config)
    # APP.run(debug=CONFIG.DEBUG, host=args.host, port=args.port)
    run_simple(
        hostname=args.host,
        port=args.port,
        application=dispatcher,
        use_debugger=CONFIG.DEBUG,
        use_reloader=True,
    )
