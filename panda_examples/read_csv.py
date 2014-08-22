__author__ = 'jason'


import pandas as pd

# Create a DataFrame from a CSV file
car_eval = pd.read_csv('car_data.txt')

# get the first 5 lines of the DataFrame
car_eval.head()
