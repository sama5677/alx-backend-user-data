from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models import storage

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a user by user_id """
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

# Define other CRUD operations (POST, PUT, DELETE) as needed

