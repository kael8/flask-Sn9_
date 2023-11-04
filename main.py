from flask import Flask, request, jsonify
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
import os

app = Flask(__name__)


@app.route('/')
def predict_sentiment():
    return jsonify({'error': 'esrtt'}), 500  # 500 is the HTTP status code for Internal Server Error


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
