import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

h_data = pd.read_csv('C:/Users/pc/Desktop/AI and ML/ML/Models/Datasets/Iowa Houses/train.csv', index_col='Id')
h_data_test = pd.read_csv('C:/Users/pc/Desktop/AI and ML/ML/Models/Datasets/Iowa Houses/test.csv', index_col='Id')
# print(h_data.head())

y = h_data.SalePrice
# print(y)

# p = y.mean()
# print(p)

h_dat_pred = h_data.drop(['SalePrice'], axis=1)

X = h_dat_pred.select_dtypes(exclude=['object'])
# print(X)

train_X, valid_X, train_y, valid_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)


def score_dataset(train_X, valid_X, train_y, valid_y):
    model = RandomForestRegressor(n_estimators=10, random_state=0)
    model.fit(train_X, train_y)
    pred = model.predict(valid_X)
    return mean_absolute_error(valid_y, pred)


"""APPROACH-1 :- DROPPING THE NULL COLUMNS"""

mis_col = [col for col in train_X.columns
           if train_X[col].isnull().any()]

dtrain_cols_X = train_X.drop(mis_col, axis=1)
dtest_cols_X = valid_X.drop(mis_col, axis=1)

print('This is the Mean Absolute Error from the first Approach:-')
print(score_dataset(dtrain_cols_X, dtest_cols_X, train_y, valid_y))

"""APPROACH-2 :- IMPUTING  THE NULL COLUMNS"""

imput_I = SimpleImputer()
impt_train_X = pd.DataFrame(imput_I.fit_transform(train_X))
impt_valid_X = pd.DataFrame(imput_I.transform(valid_X))

impt_train_X.columns = impt_train_X.columns
impt_valid_X.columns = impt_valid_X.columns

print("\n MAE from Approach 2 (Imputation):")
print(score_dataset(impt_train_X, impt_valid_X, train_y, valid_y))

"""APPROACH-3 :- IMPUTING  THE NULL COLUMNS AND KEEP TRACK OF THEM"""

train_X_plus = train_X.copy
valid_X_plus = train_X.copy

for col in mis_col:
    train_X_plus[col + 'NULL'] = train_X_plus[col].isnull()  ## ERROR:- TypeError: 'method' object is not subscriptable.
    valid_X_plus[col + 'NULL'] = valid_X_plus[col].isnull()  ## TO BE FIXED

imput_I = SimpleImputer()
impt_train_X_plus = pd.DataFrame(imput_I.fit_transform(train_X))
impt_valid_X_plus = pd.DataFrame(imput_I.transform(valid_X))

impt_train_X_plus.columns = train_X_plus.columns
impt_valid_X_plus.columns = valid_X_plus.columns

print("MAE from Approach 3 (An Extension to Imputation):")
print(score_dataset(impt_train_X_plus, impt_valid_X_plus, train_y, valid_y))
