# Import, read, and split data
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
data = pd.read_csv('data.csv')
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# Fix random seed
np.random.seed(55)

# Imports

# TODO: Uncomment one of the three classifiers, and hit "Test Run"
# to see the learning curve. Use these to answer the quiz below.

# Logistic Regression
#estimator = LogisticRegression()

# Decision Tree
#estimator = GradientBoostingClassifier()

# Support Vector Machine
#estimator = SVC(kernel='rbf', gamma=1000)
