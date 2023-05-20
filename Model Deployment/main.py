import pickle
import joblib

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, classification_report
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('C:/Users/pc/Desktop/AI and ML/ML/Datasets/Stroke Prediction/stroke-prediction-dataset/Stroke-Data_Cleaned.csv')
print(df.head(10))
#
mmScal = MinMaxScaler()

num_vars = ['gender' ,'age', 'hypertension', 'heart_disease', 'bmi', 'avg_glucose_level', 'Work']
df[num_vars] = mmScal.fit_transform(df[num_vars])

print(df.head(10))

X = df[['gender' ,'age', 'hypertension', 'heart_disease', 'bmi', 'avg_glucose_level', 'Work']]
y = df['stroke']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=1)

# """PICKLE MODEL """
# with open('finalized_model.pkl', 'rb') as file:
#     Pickled_LR_Model = pickle.load(file)

joblib_LR_model = joblib.load('joblib_RL_Model.joblib')


joblib_LR_model

score = joblib_LR_model.score(X_val, y_val)
print(score)

# # """ JOBLIB MODEL """
# joblib_file = "joblib_RL_Model.pkl"
# joblib.dump(log_reg, joblib_file)
