# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:54:37 2022

@author: Alex
"""

"""
@Title: SVM system in Molecular Biology: Classification of Splice-junction Gene Sequences
@author: LEFTERACHE Alexandru-Gabriel
@coordinating teacher:D.Eng. Corneliu-Nicolae FLOREA
"""

#imported libraries and modules
import numpy as np
from sklearn import datasets, ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#Funtion which returnes 'True' if the two lists have any elements in common
#It returnes 'False' if there are NO elements in common
def common_elements(l1, l2): 
    a_set = set(l1)          
    b_set = set(l2)
    if (a_set & b_set):
        return True
    else:
        return False

label_encoder = LabelEncoder()
ordinal_encoder = OrdinalEncoder()

data = np.genfromtxt('splice.data',dtype=None, encoding=None,delimiter=',') #Importing data
data=data[:,[0,2]]  #Reassigning data with only the first and third column
a=['D','N','S','R'] #Ambiguous characters
useful_data=[]      #Declaring useful_data
k=0 #This will track the number of rows without any ambigous characters
for i in data:
    to_be_added=i[1];                               #Assigning the DNA sequence as a string
    to_be_added=to_be_added.split()                 #Getting rid of blank spaces
    to_be_added=np.array(list(to_be_added[0]))      #Making this variable an array
    if common_elements(a, to_be_added) != True:
        to_be_added=np.append(i[0],to_be_added)     #If no ambigous characters are found => append the whole row to the new array
        useful_data = np.append(useful_data, to_be_added)
        k+=1                                        #Keeping the track of our rows
useful_data=np.reshape(useful_data, (k, 61))        #reshaping out array
X=np.array(useful_data[:,1:])   #Attributes array
Y=np.array(useful_data[:,:1])   #Labels array

X=ordinal_encoder.fit_transform(X)          #Encoding our attribtes (A->0,C->2,G->3,T->4)
Y=label_encoder.fit_transform(Y.ravel())    #Encoding our labels (EI->0,IE->1,N->2)
#Creating our training/testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.75, test_size=0.25)
#nr_trasaturi=list(range(1,101))
nr_arbori=np.arange(1,101)
in_bag=np.arange(0.05,1.05,0.05)
nr_trasaturi=np.arange(0.05,1.05,0.05)

for i in nr_arbori:
    for j in in_bag:
        #for k in nr_trasaturi:
            #print("Max samples: "+str(in_bag)+"\n")
            #clf=ensemble.BaggingClassifier(max_features=k,n_estimators=i,max_samples=j).fit(X_train,Y_train)
            clf=ensemble.BaggingClassifier(n_estimators=i,max_samples=j).fit(X_train,Y_train)
            pred=clf.predict(X_test)
            count=0
            for k in range(len(pred)):
                if(pred[k]==Y_test[k]):
                    count+=1
            print("Acuratetea pentru un numar de arbori: "+str(i)+" un procent in-bag: "+str(j)+" este: "+str(count/len(pred))+"\n")
                
