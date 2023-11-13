from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict_sentiment', methods=['POST'])
def index():
    return jsonify({'text': 'Working!!!'})

if __name__ == '__main__':
    app.run(debug=True)
