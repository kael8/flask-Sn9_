from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/sample_response')
def sample_response():
    response_data = {'message': 'This is a sample response', 'status': 'OK'}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
