import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(suppress = True) 

data = pd.read_csv("data/dane_finalne.csv", sep =";", decimal=",")
print(data.head())

# Zamienienie y na NumPy array i przekształcenie wiersza na kolumnę
y = data.Y
y = np.asarray(y.values).reshape(-1, 1)

# Dodanie kolumny
data["lnX1"] = np.log(data['X1'])

def linear_regression(data, y,):
    data = np.asarray(data.values)
    y = np.asarray(y).reshape(-1,1)
    t = data.shape[0]
    ones = np.ones(t)
    X = np.column_stack([ones, data])
    beta_head = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))
    return beta_head.round(4), X

X = data[["lnX1", "X2", "X3", "X4"]]


output, X = linear_regression(X,y)
print(output.round(3))

t = X.shape[0]
s2 = (1/(t-len(output))) * (y - X.dot(output)).T.dot(y- X.dot(output))
print(f"s = {np.sqrt(s2.round(2))}")

y_head = X.dot(output)
R2 = np.sum((y_head - np.mean(y_head))**2) / np.sum((y - np.mean(y))**2)
print(f"R2 = {R2.round(2)}")

V = np.sqrt(s2) / np.mean(y) * 100
print(f"V = {V.round(2)}")

