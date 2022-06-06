"""
@Title: SVM system in Molecular Biology: Classification of Splice-junction Gene Sequences
@author: LEFTERACHE Alexandru-Gabriel
@coordinating teacher:D.Eng. Corneliu-Nicolae FLOREA
"""

#imported libraries and modules
import numpy as np
from sklearn import svm
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

#Different values for the 'cost' parameter
cost = [1/32,1/8,1/2,2,8,32,128]
error_rates=np.array([])
for i in range(len(cost)):
    clf = svm.SVC(kernel='linear',C=cost[i]).fit(X_train, Y_train)  #Creating our SVC model
    Y_pred=clf.predict(X_test)                                      #Making predictions on our testing set
    
    #Calculating error rates using the confusion_matrix
    cm = confusion_matrix(Y_test, Y_pred)
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    error_rates=np.append(error_rates,(-1)*cm.diagonal()+1,axis=0)

    print('For a value of cost equal to: ' + str(cost[i]) + ' we have obtained:\n') #Results
    print(classification_report(Y_test, Y_pred)+'\n\n')

error_rates=np.reshape(error_rates,(len(cost),3)) #Resizing to 7x3
     
    
        

    