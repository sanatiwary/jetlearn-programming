import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# https://archive.ics.uci.edu/dataset/352/online+retail
data = pd.read_csv("Online Retail.csv")

data.columns = (
    "invoiceNo", 
    "stockCode", 
    "description", 
    "quantity", 
    "invoiceDate", 
    "unitPrice", 
    "customerId", 
    "country"
)

print(data.describe())
print(data.info())
print(data.isnull().sum())

data.dropna(inplace=True)

print(data.isin(['?']).sum())

for i in data.columns:
    print(data[i].value_counts())

countries = set(data["country"])
print(countries)

data["country"] = data["country"].map({"united kingdom": 1}).fillna(0).astype(int)

data["totalPrice"] = data["quantity"] * data["unitPrice"]

data.groupby("country").totalPrice.mean().plot(kind="bar")
plt.show()