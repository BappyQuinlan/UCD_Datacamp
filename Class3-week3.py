import pandas as pd

data = pd.read_csv("country_vaccinations.csv")

data.head()

print(data.head(5), data.shape)