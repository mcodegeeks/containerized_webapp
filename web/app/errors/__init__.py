from flask import Blueprint

bp = Blueprint('errors', __name__, template_folder='views')

from app.errors import controllers