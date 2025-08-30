from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("calorie_predictor.pkl")

@app.route('/')
def home():
    return render_template('index.html')  # Your HTML form should be in templates/index.html

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])
        heart_rate = float(request.form['heart_rate'])
        body_temp = float(request.form['body_temp'])

        # Prepare the input array
        input_data = np.array([[age, gender, height, weight, duration, heart_rate, body_temp]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        return render_template('index.html', prediction_text=f"Estimated Calories Burned: {round(prediction, 2)} kcal")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    # Use PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
