import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets


iris_DS = datasets.load_iris()

X = iris_DS.data
y = iris_DS.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 82)

from sklearn.preprocessing import StandardScaler
std_clas = StandardScaler()
X_train = std_clas.fit_transform(X_train)
X_test = std_clas.transform(X_test)

classification = GaussianNB()
classification.fit(X_train, y_train)

y_prediction = classification.predict(X_test)
print(y_prediction)

y_comparision = np.vstack((y_test,y_prediction)).T
y_comparision[:5,:]

from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_prediction)
print(conf_mat)

m = conf_mat.shape
rightPred = 0
wrongPred = 0

for row in range(m[0]):
 for i in range(m[1]):
     if row == i:
            rightPred += conf_mat[row,i]
     else:
         wrongPred += conf_mat[row,i]
print('Right predictions is', rightPred)
print('Wrong predictions is', wrongPred)
print ('\nNaive Bayes classification accuracy is ', rightPred/( conf_mat.sum()))