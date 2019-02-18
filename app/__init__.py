from flask import Flask, render_template
from app.config import base_config
from app.assets import assets

from app.blueprints.portfolio import portfolio_page

import requests

def create_app(config=base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_blueprints(app)
    register_extensions(app)
    register_jinja_env(app)
    register_errorhandlers(app)

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html.j2')

    return app

def register_extensions(app):
    assets.init_app(app)

def register_blueprints(app):
    app.register_blueprint(portfolio_page, url_prefix="/portfolio")

def register_jinja_env(app):
    app.jinja_env.globals.update({
        'site_name': app.config["SITE_NAME"],
    })

def register_errorhandlers(app):
    def render_error(error):
        return render_template('errors/%s.html.j2' % error.code), error.code

    for error in [requests.codes.INTERNAL_SERVER_ERROR, requests.codes.NOT_FOUND, requests.codes.UNAUTHORIZED]:
        app.errorhandler(error)(render_error)
