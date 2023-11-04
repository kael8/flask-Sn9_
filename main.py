from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/predict_sentiment', methods=['GET'])
def sample_response():
    mess = request.id
    response_data = {'message': 'This is a sample response 2', 'status': mess}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
