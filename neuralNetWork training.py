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

layer1=Layer("Rectifier",units=45,weight_decay=0.001)
layer2=Layer("Rectifier",units=30,weight_decay=0.001)
layer3=Layer("Softmax")

cls=Classifier(layers=[layer1,layer2,layer3],learning_rule="adam",learning_rate=0.003,f_stable=0.01,debug=True,batch_size=200,n_iter=100)
cls.fit(X_train,y_train)


# get the probability of prediction for cross data
y_predict=cls.predict_proba(X_cross,collapse=True)

print(y_predict[:,1])
p_cross=y_predict[:,1]

loss_cross=-np.multiply(y_cross,np.log(p_cross))-np.multiply(1-y_cross,np.log(1-p_cross))
print(loss_cross.sum()/loss_cross.size)

# get the probability of prediction for test data
y_predict_test=cls.predict_proba(X_test,collapse=True)

p_test=y_predict_test[:,1]

loss_test=-np.multiply(y_test,np.log(p_test))-np.multiply(1-y_test,np.log(1-p_test))
print(loss_test.sum()/loss_test.size)

# get the probability of prediction for training data
y_predict_train=cls.predict_proba(X_train,collapse=True)

p_train=y_predict_train[:,1]

loss_train=-np.multiply(y_train,np.log(p_train))-np.multiply(1-y_train,np.log(1-p_train))
print(loss_train.sum()/loss_train.size)


#parameters tuning recording
#learning_rate=0.01,f_stable=0.01,debug=True,batch_size=200,n_iter=50:
#loss_train: 0.0340, loss_cross: 0.0344, loss_test: 0.0433
#learning_rate=0.03,f_stable=0.01,debug=True,batch_size=200,n_iter=50:
#loss_train: 0.0456, loss_cross: 0.0434, loss_test: 0.0456
#learning_rate=0.003,f_stable=0.01,debug=True,batch_size=200,n_iter=50:
#loss_train: 0.0303, loss_cross: 0.0323, loss_test: 0.027
#learning_rate=0.001,f_stable=0.01,debug=True,batch_size=200,n_iter=50:
#loss_train: 0.0320, loss_cross: 0.0335, loss_test: 0.0291
#learning_rate=0.001,f_stable=0.01,debug=True,batch_size=200,n_iter=100:
#loss_train: 0.0329, loss_cross: 0.0320, loss_test: 0.0271
#learning_rate=0.003,f_stable=0.01,debug=True,batch_size=200,n_iter=100:
#loss_train: 0.0344, loss_cross: 0.0323, loss_test: 0.0294
#
#
