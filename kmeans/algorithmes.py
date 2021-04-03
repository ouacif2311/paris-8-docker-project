import numpy as np
import math as m
import pandas as pd
import numpy.random as rand


class Kmeans: 
    
    def __init__(self,k=4,max_iterint=300):
        self.k = k
        self.max_iterint = max_iterint
        
    
    def distanceEuclidienne(self,vec1,vec2):
        x=0
        nbrColonnes = len(vec1)
    
        for i in range(0,nbrColonnes):
        
            h=vec1[i]-vec2[i]
            x +=(h*h)
        d=m.sqrt(x)
        Dp=(1/(m.sqrt(self.k)))*d
        return Dp

    def centroide(self,data,y):
        z=0
        nbLignes,nbColonnes = data.shape
        C = np.zeros((self.k,nbColonnes))
        nbrExpl =np.zeros(shape=(self.k,1))
        for i in range (0,nbLignes):
            z=y[i,0]
            for j in range(0,nbColonnes):
                C[z,j] += data[i,j]
            nbrExpl[z,0]+=1
    
        for i in range (0,self.k):
            for j in range (0,nbColonnes):
                C[i,j]=C[i,j]/nbrExpl[i]
      
        return C 

    def distanceCentroideCluster(self,data,tableC):
        nbrLignes,nbrColonnes = data.shape
        ligne,colonne=tableC.shape
        DistanceFromcluster=np.zeros((nbrLignes,self.k))
    #print(DistanceFromcluster)
        for i in range (0,nbrLignes):
            for j in range (0,self.k):
                DistanceFromcluster[i,j]=self.distanceEuclidienne(data[i],tableC[j])
        return DistanceFromcluster

    def miseAJourCluster(self,DistFromCentre,y):
        ligne = len(DistFromCentre)
        for i in range(0,ligne):
            y[i] = DistFromCentre[i].argmin()
        return y

    def comparaisonCentroide(self,c,pastC):
        ligne = len(c)
        nbrCentroideStable = 0
        D = 0
        p = 0.001
        for i in range (0, ligne):
            D = self.distanceEuclidienne(c[i],pastC[i])
            if  0 <= D and D < p:
                nbrCentroideStable+=1
        if (nbrCentroideStable == self.k):
            return True
    
        return False

    def implementation (self,data):
        nbrLignes,nbrColonnes = data.shape
        yAleatoire=np.random.randint(self.k,size=(nbrLignes,1))
        pastC=np.zeros((nbrLignes,nbrColonnes))
        for i in range (0,self.max_iterint):
            tableCentroide = self.centroide(data,yAleatoire)
            if self.comparaisonCentroide(tableCentroide,pastC):
                return yAleatoire
        
            pastC=tableCentroide
            d=self.distanceCentroideCluster(data,tableCentroide)
            miseAjour=self.miseAJourCluster(d,yAleatoire)
        
        return yAleatoire