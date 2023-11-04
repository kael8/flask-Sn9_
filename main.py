from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})



if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000))
