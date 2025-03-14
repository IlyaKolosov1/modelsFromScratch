# This script generates a dataset for a linear regression model
import numpy as np
import pandas as pd


X = np.linspace(0, 45, 400)

a = 1800
b = 1
c = 1000

noise = np.random.normal(0, 200, size=len(X))

y = a * np.log(X + b) + c + noise

df = pd.DataFrame({'exp' : X, 'salary' : y})

df = df.sample(frac=1).reset_index(drop=True)

print(df.head())
df.to_csv('data.csv', index=False)
