import pandas as pd

df = pd.read_csv('G:/Softwares/Coding/SPSS/Datasets/Udemy Courses/3.1-data-sheet-udemy-courses-web-development.csv')
print(df.head(10))

print(df.columns)
print('\nLevel:', df['level'].unique())
# print('Over18:', df['Over18'].unique())
# print('OverTime:', df['OverTime'].unique())