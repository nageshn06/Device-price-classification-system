# app.py
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the model and label encoder
best_model = ...  # Load your trained model (e.g., RandomForestClassifier)
label_encoder = LabelEncoder()  # Load the encoder if necessary

# Initialize the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_price():
    # Get device specs from the POST request
    data = request.get_json()
    
    # Convert the data into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Apply label encoding to categorical columns
    categorical_columns = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']
    for col in categorical_columns:
        input_data[col] = label_encoder.transform(input_data[col])
    
    # Use the model to predict the price range
    prediction = best_model.predict(input_data)
    
    # Return the predicted price range as a JSON response
    return jsonify({"predicted_price_range": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
