import os


class base_config(object):
    SUPPORTED_LOCALES = ['en']

    SITE_NAME = os.environ.get('APP_NAME', 'Jon Kirkpatrick - Portfolio')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'itsasecret')
    SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost:5000')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


class test_config(base_config):
    TESTING = True
    WTF_CSRF_ENABLED = False
