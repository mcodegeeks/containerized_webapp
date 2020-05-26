from flask import Blueprint

bp = Blueprint('auth', __name__, template_folder='views')

from app.auth import controllers