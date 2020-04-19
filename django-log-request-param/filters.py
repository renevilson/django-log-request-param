import logging

from django_log_requests import local, response_attr, EMPTY_PARAM


class RequestIDFilter(logging.Filter):

    def filter(self, record):
        for attr in response_attr:
            setattr(record, attr, getattr(local, attr, EMPTY_PARAM))
        return True
