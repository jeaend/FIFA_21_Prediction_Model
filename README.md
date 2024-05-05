# FIFA 21 Player Overall Rating (OVA) Prediction Model

## Overview
This repository contains a prediction model for estimating the Overall Rating (OVA) of FIFA 21 players based on various attributes available on [SoFIFA](https://sofifa.com/). The model utilizes data cleaning, feature selection, and a linear regression algorithm to make predictions.

## Dataset
The dataset used in this model is sourced from [SoFIFA](https://sofifa.com/), a popular platform for FIFA player data. The dataset is stored in the `fifa21_train.csv` file.

## Data Cleaning
Before training the model, the dataset underwent several cleaning steps to ensure data quality and consistency. This included handling missing values, removing duplicates that could affect the model's performance.

## Feature Selection
Feature selection is a crucial step in building an accurate prediction model. In this project, I employed various techniques such as correlation analysis, feature importance, and domain knowledge to select the most relevant attributes for predicting player OVA ratings.

## Feature Selection
During the exploratory data analysis (EDA) phase, it became apparent that many columns exhibited a low correlation with the target variable, OVA (Overall Rating). However, amidst this, a new column was introduced to represent the score for the best noted position, which displayed a notably strong correlation with the OVA. Recognizing its potential as a valuable predictor for OVA, the decision was made to incorporate this new feature into the analysis. 

## Linear Regression Model
I chose a linear regression model for its simplicity and interpretability. The model aims to establish a linear relationship between the selected features and the target variable (OVA rating). I trained the model using the cleaned dataset and evaluated its performance using appropriate metrics such as mean squared error (MSE) and R-squared.

## Usage
To use the prediction model:
1. Clone this repository to your local machine.
2. Ensure that the `fifa21_train.csv` dataset file is in the appropriate directory.
3. Run the `train_model.py` script to train the linear regression model.
4. Once trained, you can use the model to make predictions by running the `unpickle_model.py` script and providing input data (setup with `fifa21_validate.csv`).

## Results
After training and evaluating the model, I have achieved satisfactory performance in predicting player OVA ratings.

## Limitations
This project focuses on implementing a basic linear regression model without advanced preprocessing techniques such as normalization, scaling, etc. The aim is to build a simple yet effective predictive model for estimating FIFA 21 player OVA ratings.