import pandas as pd

df = pd.read_csv('./winequality-red.csv')

print(df[df['quality'] >= 7])
