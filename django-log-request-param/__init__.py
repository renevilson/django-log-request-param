import threading
from django.conf import settings

__version__ = "1.0.0"
local = threading.local()

REQUEST_ID_HEADER = getattr(settings, "REQUEST_ID_HEADER", "HTTP_X_REQUEST_ID")
EMPTY_PARAM = getattr(settings, "EMPTY_PARAM", "-")
REQUEST_METHOD = getattr(settings, "REQUEST_METHOD", "method")
PATH_INFO = getattr(settings, "PATH_INFO", "path_info")

USER_ID = getattr(settings, "USER_ID", "id")
USER_NAME = getattr(settings, "USER_NAME", "username")
USER_EMAIL = getattr(settings, "USER_EMAIL", "email")
USER_PHONE = getattr(settings, "USER_PHONE", "phone")
HTTP_USER_AGENT = getattr(settings, "HTTP_USER_AGENT", "HTTP_USER_AGENT")
SERVER_PROTOCOL = getattr(settings, "SERVER_PROTOCOL", "SERVER_PROTOCOL")
REMOTE_ADDR = getattr(settings, "REMOTE_ADDR", "REMOTE_ADDR")

response_attr = [
    "request_id", "request_method", "path_info", "user_id", "username", "email", "phone",
    "user_agent", "server_protocol", "remote_addr",
]
