import sys
import os
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, request, jsonify
from DataStrcutures.StaticArrayStack import StaticArrayStack

ds_api = Blueprint('ds_api', __name__)
stack = StaticArrayStack(100) 

@ds_api.route('/stack/push', methods=['POST'])
def push_stack():
    try:
        data = request.json
        value = data.get('value')
        if value is not None:
            stack.push(value)
            return jsonify({"stack": stack.to_list(), "success": True})
            # 200 OK (default for successful responses)
            # 400 Bad Request (when no value is provided or the stack is empty)
            # 500 Internal Server Error (for other exceptions)
        else:
            return jsonify({"error": "No value provided", "stack": stack.to_list()}), 400
    except Exception as e:
        return jsonify({"error": str(e), "stack": stack.to_list()}), 500

@ds_api.route('/stack/pop', methods=['POST'])
def pop_stack():
    try:
        if not stack.is_empty():
            stack.pop()
            return jsonify({"stack": stack.to_list(), "success": True})
        else:
            return jsonify({"error": "Stack is empty", "stack": []}), 400
    except Exception as e:
        return jsonify({"error": str(e), "stack": stack.to_list()}), 500

# Add a route to get current stack state
@ds_api.route('/stack', methods=['GET'])
def get_stack():
    return jsonify({"stack": stack.to_list()})
