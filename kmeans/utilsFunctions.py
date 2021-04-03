import numpy as np
import math as m
import pandas as pd

def moyenne(x):
    moy=(np.sum(x)/len(x))
    return moy

def variance(x,y):
    var=0
    for i in range(0,len(x)):  
        var+=(x[i]-y)*(x[i]-y)*(1/len(x))
    return var
    
def ecarttype(y):
    e=np.sqrt(y)
    return e

def covariance(tab,tab2,moy1,moy2):
    cov=0
    n=0
    for i in range(0,len(tab)):
        n+=(tab[i]-moy1)*(tab2[i]-moy2)
        cov=(1/150)*n
    return cov

def coeffecientCorrélation(cov,ecartType1,ecartType2):
    coeff=cov/(ecartType1*ecartType2)
    return coeff

def convert_iris_data_class(a):
    if (a == "Iris-setosa"): 
        return 0
    if (a == "Iris-versicolor"): 
        return 1
    if (a == "Iris-virginica"): 
        return 2