"""
A weighted version of categorical_crossentropy for keras (1.1.0). This lets you apply a weight to unbalanced classes.
@url: https://gist.github.com/wassname/ce364fddfc8a025bfab4348cf5de852d
@author: wassname
"""
from keras import backend as K
class weighted_categorical_crossentropy(object):
    """
    A weighted version of keras.objectives.categorical_crossentropy
    
    Variables:
        weights: numpy array of shape (C,) where C is the number of classes
    
    Usage:
        loss = weighted_categorical_crossentropy(weights).loss
        model.compile(loss=loss,optimizer='adam')
    """
    
    def __init__(self,weights):
        self.weights = K.variable(weights)
        
    def loss(self,y_true, y_pred):
        # scale preds so that the class probas of each sample sum to 1
        y_pred /= y_pred.sum(axis=-1, keepdims=True)
        # clip
        y_pred = K.clip(y_pred, K.epsilon(), 1)
        # calc
        loss = y_true*K.log(y_pred)*self.weights
        loss =-K.sum(loss,-1)
        return loss
    

    


# test that it works that same as categorical_crossentropy with weights of one
import numpy as np
from keras.activations import softmax
from keras.objectives import categorical_crossentropy

samples=3
maxlen=4
vocab=5

y_pred_n = np.random.random((samples,maxlen,vocab))
y_pred = K.variable(y_pred_n)
y_true_n = softmax(np.random.random((samples,maxlen,vocab))).eval()
y_true = K.variable(y_true_n) # this isn't binary
weights = np.ones(vocab)

r=weighted_categorical_crossentropy(weights).loss(y_true_n,y_pred_n).eval()
rr=categorical_crossentropy(y_true_n,y_pred_n).eval()
np.testing.assert_almost_equal(r,rr)
print('OK')