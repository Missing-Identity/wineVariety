from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

app = Flask(__name__)

# Load the model and the LabelEncoder from pickle files
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('labelencoder.pkl', 'rb') as f:
    le = pickle.load(f)
with open('columns.pkl', 'rb') as f:
    train_columns = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Preprocess the data
    data_encoded = data.copy()
    known_labels = set(le.classes_)
    data_encoded = pd.get_dummies(data_encoded, columns=['country', 'province'])
    data_tfidf = vectorizer.transform([data['review_description']])
    data_tfidf = pd.DataFrame(data_tfidf.toarray(), columns=vectorizer.get_feature_names_out())
    # Ensure the encoded data has the same columns as the training data
    missing_cols = set(train_columns) - set(data_encoded.columns)
    for c in missing_cols:
        data_encoded[c] = 0
    data_encoded = data_encoded[train_columns]

    # Fill NaN values with 0
    data_encoded = data_encoded.fillna(0)

    data_combined = pd.concat([data_encoded, data_tfidf], axis=1)

    # Make a prediction using the model
    prediction = model.predict(data_combined)

    # Send the prediction back as json
    return jsonify({'variety': prediction[0]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
