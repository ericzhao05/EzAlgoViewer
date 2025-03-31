from flask import Flask, jsonify
from flask_cors import CORS

# Import your routes from the api folder
from api.ds_routes import ds_api  # a Blueprint (like a route module)

app = Flask(__name__)
CORS(app)  # Allow React (port 3000) to talk to Flask (port 5000)

# Register the routes with a prefix
app.register_blueprint(ds_api, url_prefix="/api")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
