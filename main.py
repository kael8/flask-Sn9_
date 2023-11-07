from flask import Flask, jsonify
import os


app = Flask(__name__)

# API endpoint to predict sentiment
@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():


    
    return jsonify({'text': 'connected')})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
