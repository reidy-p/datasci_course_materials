import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, confusion_matrix

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
print(train_df.head())
print(train_df.dtypes)
print(train_df.corr())

# Use numeric features only
numeric_cols = ['Survived', 'Age', 'SibSp', 'Parch', 'Fare']
numeric_cols = ['Survived', 'Age', 'Fare']
model1_train_df = train_df[numeric_cols].dropna()
X = model1_train_df[model1_train_df.columns.difference(['Survived'])] 
y = model1_train_df['Survived']
lr = LogisticRegression()
lr.fit(X, y)

print(accuracy_score(y, lr.predict(X)))
print(confusion_matrix(y, lr.predict(X)))

# Use numeric and categorical features 
full_cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
model2_train_df = train_df[full_cols].dropna()
model2_train_df = pd.get_dummies(model2_train_df, columns=['Pclass', 'Sex', 'Embarked'])
X = model2_train_df[model2_train_df.columns.difference(['Survived'])] 
y = model2_train_df['Survived']

lr = LogisticRegression()
lr.fit(X, y)
print(accuracy_score(y, lr.predict(X)))
print(confusion_matrix(y, lr.predict(X)))

svm = SVC()
svm.fit(X, y)
print(accuracy_score(y, svm.predict(X)))
print(confusion_matrix(y, svm.predict(X)))

# Test data
cols = ['Sex', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
test_df = test_df[cols].dropna()
test_df = pd.get_dummies(test_df, columns=['Pclass', 'Sex', 'Embarked'])
X = test_df[test_df.columns.difference(['Survived'])] 
svm.predict(X)

