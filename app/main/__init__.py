from flask import Blueprint

bp = Blueprint('simple_page', __name__, template_folder='templates')

from app.main import routes
