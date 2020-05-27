from app.api import bp

## CRUD

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass

'''
/api    The API entry point
/api/:coll  A top-level collection named “coll”
/api/:coll/:id  The resource “id” inside collection “coll”
/api/:coll/:id/:subcoll Sub-collection “subcoll” under resource “id”
/api/:coll/:id/:subcoll/:subid  The resource “subid” inside “subcoll”
'''