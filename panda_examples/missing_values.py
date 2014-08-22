__author__ = 'jason'

from pandas import pd

car_eval_missing = pd.read_csv('')

# shows if there is any missing data for the columns specified
pd.isnull(car_eval_missing).any()

# remove missing values

shape = car_eval_missing.shape

car_eval_missing = car_eval_missing.dropna(how='any')
