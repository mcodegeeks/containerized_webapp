from flask import jsonify
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return jsonify(hello="world")