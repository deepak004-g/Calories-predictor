from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("calorie_predictor.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        gender = float(request.form['gender'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        duration = float(request.form['duration'])
        heart_rate = float(request.form['heart_rate'])
        body_temp = float(request.form['body_temp'])
        
        input_data = np.array([[age, gender, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(input_data)
        result = round(prediction[0], 2)
    except Exception as e:
        result = "Error: " + str(e)
    
    return render_template('index.html', prediction_text=f"Calories Burned: {result}")

if __name__ == "__main__":
    app.run(debug=True)
