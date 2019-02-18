import requests
import logging
import sys

from flask import Flask, render_template
from app.config import base_config, test_config
from app.assets import assets
from app.blueprints.portfolio import portfolio


def create_app(config=base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_env(app)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html.j2')

    @app.errorhandler(500)
    def error_500(error):
        return render_template('errors/500.html.j2'), error.code

    return app


def register_extensions(app):
    assets.init_app(app)


def register_blueprints(app):
    app.register_blueprint(portfolio, url_prefix="/portfolio")


def register_jinja_env(app):
    app.jinja_env.globals.update({
        'site_name': app.config["SITE_NAME"],
    })


def register_errorhandlers(app):
    def render_error(error):
        return render_template(
            'errors/%s.html.j2' % error.code
        ), error.code

    for error in [
        requests.codes.INTERNAL_SERVER_ERROR,
        requests.codes.NOT_FOUND,
        requests.codes.UNAUTHORIZED
    ]:
        app.errorhandler(error)(render_error)
