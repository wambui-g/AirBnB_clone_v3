#!/usr/bin/python3
"""states view of the api"""
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state():
    """retrieves list of all states"""
    objs = storage.all(State)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def one_state(state_id):
    """retrieves state based on id"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/state/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_state(state_id):
    """Deletes state as per ID given"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/state', methods=['POST'], strict_slashes=False)
def post_state():
    """Creates a state"""
    new_state = request.get_json()
    if not new_state:
        abort(400, "Not JSON")
    if 'name' not in new_state:
        abort(400, "Missing name")
    obj = State(**new_state)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/state/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """Updates state object"""
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not JSON")

    for i, j in req.items():
        if i not in ['id', 'created_at', 'updated_at']:
            setattr[obj, i, j]

    storage.save()
    return make_response(jsonify(obj.to_dict()), 200)
