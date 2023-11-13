from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/predict_sentiment', methods=['POST'])
def index():
    return jsonify({'text': 'Working!!!'})

if __name__ == '__main__':
    app.run(debug=True)
