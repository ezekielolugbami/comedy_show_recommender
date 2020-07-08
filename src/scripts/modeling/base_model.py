# import necessary libraries
from pyprojroot import here
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# Load processed input and target
data_input = pd.read_csv(here('./data/processed/data_input.csv'))
data_label = pd.read_csv(here('./data/processed/data_label.csv'), header=None)


print(data_input.shape)
data_input.head(3)

data_label.head(3)


# Spliting into train and test set
X_train, X_test, y_train, y_test = train_test_split(data_input, data_label, test_size=0.25, random_state=2)
print('Train set shape: ', X_train.shape)
print('Test set shape: ', X_test.shape)


# Training the model
regressor = RandomForestRegressor(random_state=0, max_depth=8)
regressor.fit(X_train, y_train)


# Evaluating model performance
score = cross_val_score(estimator=regressor,X=X_train, y=y_train, cv=5, scoring="neg_mean_squared_error")
score = -1 * np.mean(score)
print("RMSE is {}".format(score))


#Save the model
import pickle
filename = 'ranF_model.pkl'
pickle.dump(regressor, open(here('./outputs/models/'+filename), 'wb'))


