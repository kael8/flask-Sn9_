from flask import Flask, request, jsonify
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"wregwsfnj": "rfhirtm"})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
