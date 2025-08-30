#generic libaries
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
import joblib

#loading the data from csv file to a Pandas Dataframe
calories = pd.read_csv('/Users/deepak/web development learning/calorie/calories.csv')

#Print first 5 rows of Data frame
print(calories.head())

exercise_data = pd.read_csv('/Users/deepak/web development learning/calorie/exercise.csv')
print(exercise_data.head())

#Converting Gender column (Male -> 0, Female -> 1)
exercise_data['Gender'] = exercise_data['Gender'].map({'male': 0, 'female': 1})

#Combinig the two data frame
calories_data = pd.concat([exercise_data,calories['Calories']], axis=1)
# print(calories_data.head())
# print(calories_data.shape)
# print(calories_data.info())
# print(calories_data.isnull().sum())

#statistical measure about the data
print(calories_data.describe())
sns.set()
#plotting the gender column in count plot
# sns.countplot(x='Age', data=calories_data)
# plt.show()
# sns.displot(calories_data['Height'])
# plt.show()

#constructing a heatmap
correlation = calories_data.corr()  

# plt.figure(figsize=(10,10))
# sns.heatmap(correlation, cbar=True, square=True, annot=True, annot_kws={"size":8}, cmap="Blues")
# plt.show()

# Features (independent variables)
x = calories_data.drop(columns=['User_ID','Calories'], axis=1)

# Target (dependent variable)
y = calories_data['Calories']

# Print to check
print(x.head())
print(y.head())

#splleting the data 
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2 , random_state=2)
print(x.shape,x_train.shape,x_test.shape)

#model training
#loadiing the model 
model = XGBRegressor()

#training the model with x train 
model.fit(x_train,y_train)

# prediction oon test value
test_data_prediction = model.predict(x_test)
print(test_data_prediction)

#Mean Abosolute Error
mae = metrics.mean_absolute_error(y_test,test_data_prediction)
print("mean aboslute error =", mae)

new_data = np.array([[25, 0, 175, 70, 30, 100, 38.5]])
prediction = model.predict(new_data)
print("Calories Burned:", prediction)
joblib.dump(model, "calorie_predictor.pkl")
