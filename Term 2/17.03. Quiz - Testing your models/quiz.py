# Import statements
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Import the train test split
# http://scikit-learn.org/0.16/modules/generated/sklearn.cross_validation.train_test_split.html


# Read in the data.
data = np.asarray(pd.read_csv('data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y.
X = data[:, 0:2]
y = data[:, 2]

# Use train test split to split your data
# Use a test size of 25% and a random state of 42
X_train, X_test, y_train, y_test =

# Instantiate your decision tree model
model = None

# TODO: Fit the model to the training data.

# TODO: Make predictions on the test data
y_pred = None

# TODO: Calculate the accuracy and assign it to the variable acc on the test data.
acc = None
