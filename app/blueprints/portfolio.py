from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

portfolio_page = Blueprint('portfolio_page', __name__,
                        template_folder='templates')

@portfolio_page.route('/')
def portfolio_index():
    return render_template('portfolio/index.html.j2')
