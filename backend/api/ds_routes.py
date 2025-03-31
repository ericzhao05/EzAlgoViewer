from flask import Blueprint, request, jsonify
from DataStrcutures.StaticArrayStack import StaticArrayStack  # fixed import

ds_api = Blueprint('ds_api', __name__)
stack = StaticArrayStack(100)  # Changed from Stack to StaticArrayStack

@ds_api.route('/stack/push', methods=['POST'])
def push_stack():
    data = request.json
    value = data.get('value')
    stack.push(value)
    return jsonify({"stack": stack.to_list()})

@ds_api.route('/stack/pop', methods=['POST'])
def pop_stack():
    stack.pop()
    return jsonify({"stack": stack.to_list()})
