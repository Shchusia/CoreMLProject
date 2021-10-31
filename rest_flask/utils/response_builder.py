import os
import traceback
from typing import Any, Dict, Optional

from werkzeug import import_string

CONFIG = import_string(os.getenv("APP_SETTINGS", "rest_flask.config.Config"))


def bad_response(
    code: int = 400, title: str = "", detail: str = "", exc: Optional[Exception] = None
) -> Dict[str, Any]:
    if CONFIG.IS_PRINT_ERROR_IN_MSG and exc:
        str_traceback = "".join(
            traceback.format_exception(
                type(exc),
                exc,
                exc.__traceback__,
            )
        )
        detail += f"{str(exc)}" f" Traceback: {str_traceback}"

    response = dict(status="error", error=dict(code=code, title=title, detail=detail))
    return response


def good_response(data) -> Dict[str, Any]:
    response = dict(status="success", data=data)
    return response
