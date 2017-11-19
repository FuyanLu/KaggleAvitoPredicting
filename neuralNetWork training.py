# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:13:56 2017

@author: Fuyan

"""


import numpy as np

from sklearn.cross_validation import train_test_split as tts
from sknn.mlp import Classifier, Layer


# importing data as numpy array

data=np.loadtxt("C:\\Users\\Fuyan\\Desktop\\avito-context-ad-clicks\\newdata.text")
   
print(np.array2string(data[1,:]))

# get data size m*n
m,n=data.shape

print(m)
print(n)

X=data[:,0:n-1]
y=data[:,n-1]

# Split data as training-set and test-set

X_train, X_test, y_train, y_test=tts(X,y,test_size=0.4,random_state=0)

X_cross, X_test, y_cross, y_test=tts(X_test,y_test,test_size=0.5,random_state=0)

print(y_train.shape)
print(y_test.shape)
print(y_cross.shape)

# build multiple layers perceptron classifier

layer1=Layer("Rectifier",units=45,weight_decay=0.0001)
layer2=Layer("Rectifier",units=30,weight_decay=0.0001)
layer3=Layer("Softmax")

cls=Classifier(layers=[layer1,layer2,layer3],learning_rule="adam",learning_rate=0.002,f_stable=0.001,debug=True)
cls.fit(X_train,y_train)


