import joblib
import numpy as np

# Load the trained model
model = joblib.load("calorie_predictor.pkl")

# Example input data (Age, Gender, Height, Weight, Duration, Heart_Rate, Body_Temp)
# Gender: male=0, female=1
new_data = np.array([[25, 0, 175, 70, 30, 100, 38.5]])

# Predict
prediction = model.predict(new_data)
print("Calories Burned:", prediction[0])
