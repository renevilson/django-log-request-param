from django_logger import local, EMPTY_PARAM, REQUEST_METHOD, PATH_INFO, USER_ID, USER_NAME, USER_EMAIL, \
    USER_PHONE, HTTP_USER_AGENT, SERVER_PROTOCOL, REMOTE_ADDR

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(local, "request", request)
        self._add_attributes(local)

    @staticmethod
    def process_response(request, response):
        return response

    @staticmethod
    def _add_attributes(record):
        request = getattr(record, "request", object)
        setattr(record, "request_method", getattr(request, REQUEST_METHOD, EMPTY_PARAM))
        setattr(record, "path_info", getattr(request, PATH_INFO, EMPTY_PARAM))

        user = getattr(request, "user", None)
        if user and not user.is_anonymous:
            setattr(record, "user_id", getattr(user, USER_ID, EMPTY_PARAM))
            setattr(record, "username", getattr(user, USER_NAME, EMPTY_PARAM))
            setattr(record, "email", getattr(user, USER_EMAIL, EMPTY_PARAM))
            setattr(record, "phone", getattr(user, USER_PHONE, EMPTY_PARAM))

        meta = getattr(request, "META", {})
        setattr(record, "user_agent", meta.get(HTTP_USER_AGENT, EMPTY_PARAM))
        setattr(record, "server_protocol", meta.get(SERVER_PROTOCOL, EMPTY_PARAM))
        setattr(record, "remote_addr", meta.get(REMOTE_ADDR, EMPTY_PARAM))
