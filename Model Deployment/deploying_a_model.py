"""# **Final Model**"""

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, GridSearchCV
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error, classification_report
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('C:/Users/pc/Desktop/AI and ML/ML/Datasets/Stroke Prediction/stroke-prediction-dataset/Stroke-Data_Cleaned.csv')
df.head(10)

"""## Scaling"""

mmScal = MinMaxScaler()

num_vars = ['gender' ,'age', 'hypertension', 'heart_disease', 'bmi', 'avg_glucose_level', 'Work']
df[num_vars] = mmScal.fit_transform(df[num_vars])

df.head(10)

X = df[['gender' ,'age', 'hypertension', 'heart_disease', 'bmi', 'avg_glucose_level', 'Work']]
y = df['stroke']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=1)

# Linear Regression

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

y_pred_lr = model_lr.predict(X_val)


# Logistic Regression

model_lor = LogisticRegression()
model_lor.fit(X_train, y_train)

y_pred_lor = model_lor.predict(X_val)

print('LR: ', mean_absolute_error(y_pred_lr, y_val), '\nLOR: ', mean_absolute_error(y_pred_lor, y_val))

print(mean_squared_error(y_pred_lr, y_val), mean_squared_error(y_pred_lor, y_val))

"""## Cross Validation"""

lr_cv = cross_val_score(model_lr, X_train, y_train, cv=10)
lor_cv = cross_val_score(model_lor, X_train, y_train, cv=10)

print('lrcv: ', lr_cv.mean(), '\nlorcv: ', lor_cv.mean())

model_lor_cv = LogisticRegression(random_state=42)
# model_lor_Cv.fit(X_train, y_train)

# y_pred_lor_cv = model_lor_Cv.predict(X_val)

log_reg_params = {"penalty": ['l1'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

grid_log_reg = GridSearchCV(LogisticRegression(solver='liblinear'), log_reg_params)
grid_log_reg.fit(X_train, y_train)
# We automatically get the logistic regression with the best parameters.
log_reg = grid_log_reg.best_estimator_

y_pred_lor_cv = log_reg.predict(X_val)

y_val

print('LOR: ', mean_absolute_error(y_pred_lor_cv, y_val))

p_lor_cv = pd.DataFrame({'Real':y_val, 'Pred':y_pred_lor_cv})
p_lor_cv = p_lor_cv.sort_values(by='Real')
p_lor_cv = p_lor_cv.reset_index()

plt.figure(figsize=(15, 5))
plt.plot(p_lor_cv['Pred'], label='pred')
plt.plot(p_lor_cv['Real'], label='actual')
plt.legend()
plt.show()

log_reg_score = cross_val_score(log_reg, X_train, y_train, cv=5)
print('Logistic Regression Cross Validation Score: ', round(log_reg_score.mean() * 100, 2).astype(str) + '%')

print('Logistic Regression:')
print(classification_report(y_val, y_pred_lor_cv))

# print(model_lor_cv.get_params().keys())


# PICKLE MODEL
import pickle

filename = 'finalized_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(log_reg, file)

# res = model.predict(X_val, y_val)
# print(res)

# # JOBLIB MODEL
# import joblib
#
# joblib_file = "joblib_RL_Model.pkl"
# joblib.dump(LR_Model, joblib_file)
