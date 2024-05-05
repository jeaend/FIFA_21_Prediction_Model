import pandas as pd
import numpy as np
import joblib
import clean_test_data_functions as clean_data

# load the trained model
model = joblib.load('linear_regression_model.pkl')

# load input data
data = pd.read_csv('fifa21_validate.csv')

# preprocess input data 
data = clean_data.clean_fifa_data(data)
y = data['OVA']
X = data.drop(['OVA'], axis=1)
X = X.select_dtypes(include = np.number)

# make predictions
predictions = model.predict(data)

# output predictions
print(predictions)
