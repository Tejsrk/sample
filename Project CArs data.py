#Cars Data Analysis
import pandas as pd
car = pd.read_csv(r"C:\Users\TEJAS RAO K\Downloads\2. Cars Data1.csv")
car.head()

#Data cleaning
car.isnull()
car.isnull().sum()

#removing unwanted records
car['Weight'] > 4000

car[~(car['Weight'] > 4000)]