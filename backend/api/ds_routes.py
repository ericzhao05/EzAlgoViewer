import sys
import os
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, request, jsonify
from DataStrcutures.StaticArrayStack import StaticArrayStack
from DataStrcutures.StaticArrayQueue.py import StaticArrayQueue
from DataStrcutures.ArrayQueue.py import ArrayQueue

ds_api = Blueprint('ds_api', __name__)
stack = StaticArrayStack(100) 
staticQueue = StaticArrayQueue(100) # try to implement that the size of the queue will be customized by the user

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

@ds_api.route("/staticQueue", methods=['GET'])
def get_static_queue():
    return jsonify({"staticQueue": staticQueue.to_list()})

@ds_api.route("/staticQueue/enqueue", method=["POST"])
def enqueueStaticQueue():
    try:
        data = request.json
        value = data.get("value")
        if value is not None:
            staticQueue.enqueue(value)
            return jsonify({"staticQueue": staticQueue.to_list(), "success": True})
        else: 
            return jsonify({"error": "No value provided", "staticQueue": stack.to_list()})
    except Exception as e:
        return  jsonify({"error": str(e), "staticQueue": staticQueue.to_list()})
    
@ds_api.route("/staticQueue/dequeue", method=[POST])
def dequeueStaticQueue():
    try:
        if not staticQueue.is_empty:
            staticQueue.dequeue()
            return jsonify({"staticQueue": staticQueue.to_list(), "success": True})
        else:                          
            return jsonify({"error": "Queue is empty", "Queue": []}), 400
    except Exception as e:
        return jsonify({"error": str(e), "stack": stack.to_list()}), 500
        
    
