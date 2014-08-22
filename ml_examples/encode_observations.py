__author__ = 'jason'

import pandas as pd

# Create a DataFrame from a CSV file
car_data = pd.read_csv('car_data.txt')

# get the first 5 lines of the DataFrame
car_data.head()


from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()

car_data = vec.fit_transform(car_data).toarray()

