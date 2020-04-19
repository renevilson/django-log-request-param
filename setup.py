from __future__ import print_function

from setuptools import setup
import os


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


setup(
    name="django-log-request-param",
    version="1.0",
    url="https://gitlab.com/ReneVilson/django_logger",
    author="renevilson",
    author_email="vildanovrinat94@gmail.com",
    packages=get_packages("django_log_requests"),
)
