import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib
import clean_test_data_functions as clean_data

# load the dataset
data = pd.read_csv('fifa21_train.csv')

# preprocessing
data = clean_data.clean_fifa_data(data)
y = data['OVA']
X = data.drop(['OVA'], axis=1)
X = X.select_dtypes(include = np.number)


# train the linear regression model
model = LinearRegression()
model.fit(X, y)

# save the trained model
joblib.dump(model, 'linear_regression_model.pkl')
