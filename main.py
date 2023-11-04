from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/')
def predict_sentiment():
    return jsonify({'error': 'esrtt'}), 500  # 500 is the HTTP status code for Internal Server Error


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
