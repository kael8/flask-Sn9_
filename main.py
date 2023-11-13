from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_sentiment', methods=['POST'])
def index():
    # Get the 'text' from the POST request
    data = request.json
    text_from_request = data.get('text', 'No text provided')

    # Use the received text in the response
    response_data = {'text': f'Received: {text_from_request}'}

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
