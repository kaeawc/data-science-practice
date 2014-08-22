
__author__ = 'jason'


import pandas as pd

# Create a DataFrame from a CSV file
car_eval = pd.read_csv('car_data.txt')

# get the first 5 lines of the DataFrame
car_eval.head()

pivoted_car = car_eval.pivot_table(values='doors', rows='lug_boot', cols='class', aggfunc='mean')


print(pivoted_car)