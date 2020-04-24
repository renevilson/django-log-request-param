Django-log-request-param
========================
**It's a middleware for logging requests. There are few parameters that you can log:**
1. request_id
2. request_method
3. path_info
4. user_id
5. username
6. email
7. phone
8. user_agent
9. server_protocol
10. remote_addr


Django settings
---------------
On django settings you can override search parameters.
<br>
There are parameters than you can use:

1. **REQUEST_ID_HEADER**. Default value: "HTTP_X_REQUEST_ID"
2. **REQUEST_METHOD**. Default value: "method"
3. **PATH_INFO**. Default value: "path_info"
4. **USER_ID**. Default value: "id"
5. **USER_NAME**. Default value: "username"
6. **USER_EMAIL**. Default value: "email"
7. **USER_PHONE**. Default value: "phone"
8. **HTTP_USER_AGENT**. Default value: "HTTP_USER_AGENT"
9. **SERVER_PROTOCOL**. Default value: "SERVER_PROTOCOL"
10. **REMOTE_ADDR**. Default value: "REMOTE_ADDR"
11. **EMPTY_PARAM**. Default value: "-". Parameter for None result.

Installation and usage
----------------------

First of all you need to install package. Download package, and install with pip: `pip install -e path/to/package`.

Secondly, need to add middleware class to your `MIDDLEWARE_CLASSES`:
```python
MIDDLEWARE_CLASSES = [
    ...,
    "django_logger.middleware.RequestMiddleware",
    ...,
]
```

Configure LOGGING settings. Add to filters:
```python
LOGGING = {
    # other settings
    'filters': {
        'request_id': {
            '()': 'django_logger.filters.RequestIDFilter'
        }
    },
    # other settings
}
```
Add params to formatter:
```python
LOGGING = {
    # other settings
    'filters': {
        'request_id': {
            '()': 'django_logger.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': ''  # Params that you want to see in yor logs
        },
    },
}
```
