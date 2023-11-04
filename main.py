from flask import Flask, request, jsonify
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
import os

app = Flask(__name__)


@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    data = request.get_json(force=True)
    text = data['text']
    return jsonify({"fdfg":"sgsed"})
    # Convert new texts to sequences using the loaded tokenizer
    new_sequences = tokenizer.texts_to_sequences([text])

    # Map out-of-vocabulary words to a special token
    for i, seq in enumerate(new_sequences):
        new_sequences[i] = [token if 1 <= token <= tokenizer.num_words else 1 for token in seq]

    max_sequence_length = 100

    # Pad sequences to have a consistent length
    new_X = pad_sequences(new_sequences, maxlen=max_sequence_length)

    # Predict using the loaded model
    predictions = model.predict(new_X)

    # Determine sentiment based on the prediction
    sentiment = "Positive" if predictions[0][0] >= 0.5 else "Negative"
    
    return jsonify({'text': text, 'predicted_sentiment': sentiment, 'prediction_score': float(predictions[0][0])})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
