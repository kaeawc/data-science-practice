__author__ = 'jason'

import pandas as pd
car_data_training = pd.read_csv('car_data_training.txt')
car_data_test = pd.read_csv('car_data_test.txt')
target_train = pd.read_csv('target_train.txt')

from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()

car_data = vec.fit_transform(car_data_test).toarray()

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

nb.fit(car_data_training, target_train)

pred = nb.predict(car_data)



