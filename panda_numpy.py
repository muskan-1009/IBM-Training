import numpy as np
import pandas as pd

# QUESTION 1

df= pd.read_csv("E:\Training\products.csv")
print(df)

average_price = np.mean(df['Price'])
print("Average Price =", average_price)

def products_above_average(dataframe):
    print("\nProducts priced above average:")
    
    for index, row in dataframe.iterrows(): # iterrows is a python method used to iterate through the rows in the dataframe.
        if row['Price'] > average_price:
            print(row['Product_Name'], "-", row['Price'])

products_above_average(df)

# QUESTION 2

df1= pd.read_csv("E:\\Training\\temperature.csv")
print(df1)

highest_temp = np.max(df1['Temperature'])
lowest_temp = np.min(df1['Temperature'])
average_temp = np.mean(df1['Temperature'])

print("Highest Temperature:", highest_temp, "°C")
print("Lowest Temperature:", lowest_temp, "°C")
print("Average Temperature:", average_temp, "°C")

def classify_temperature(temp):
    if temp < 20:
        return "Cold"
    elif 20 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"

# Display category for each day
print("\nTemperature Categories:")
for index, row in df1.iterrows():
    category = classify_temperature(row['Temperature'])
    print(row['Day'], "-", row['Temperature'], "°C :", category)