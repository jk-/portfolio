from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

portfolio = Blueprint('portfolio', __name__,
                        template_folder='templates')

@portfolio.route('/')
def index():
    return render_template('portfolio.html.j2')
