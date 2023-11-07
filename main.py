from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    text = request.json['text']
    # Perform sentiment analysis here
    sentiment = text  # This should be replaced with actual sentiment analysis result
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
