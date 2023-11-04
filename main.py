from flask import Flask, request, jsonify
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer

app = Flask(__name)
@app.route('/')
def index():
    return jsonify({"wregwsfnj": "rfhirtm"})
# Load and merge the partitioned tokenizer states
tokenizer_state_filenames = [
    'model/tokenizer_state_part0.pkl',
    'model/tokenizer_state_part1.pkl'
]

# Initialize an empty tokenizer
tokenizer = Tokenizer()
tokenizer.word_index = {}
tokenizer.index_word = {}
tokenizer.word_counts = {}
tokenizer.document_count = 0

# Iterate through each part, load it, and merge it into the complete tokenizer
for part_filename in tokenizer_state_filenames:
    with open(part_filename, 'rb') as handle:
        part_tokenizer_state = pickle.load(handle)
        
    part_tokenizer = Tokenizer()
    part_tokenizer.__dict__.update(part_tokenizer_state)
    
    # Merge the part tokenizer into the complete tokenizer
    tokenizer.word_index.update(part_tokenizer.word_index)
    tokenizer.word_counts.update(part_tokenizer.word_counts)
    tokenizer.document_count += part_tokenizer.document_count

# Set the num_words attribute based on your previous information
tokenizer.num_words = 10000

# Load the trained model
model_filename = 'model/sentiment_analysis_model.h5'
model = load_model(model_filename)

# Manually inserted text for sentiment analysis
manually_inserted_text = "This is a great product. I love it!"

# Convert new texts to sequences using the loaded tokenizer
new_sequences = tokenizer.texts_to_sequences([manually_inserted_text])

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

print(f'Manually Inserted Text: {manually_inserted_text}')
print(f'Predicted Sentiment: {sentiment}')
print(f'Prediction Score: {float(predictions[0][0])}')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
