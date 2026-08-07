# backend/index.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables React to fetch from this backend without CORS errors

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the Flask backend!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
