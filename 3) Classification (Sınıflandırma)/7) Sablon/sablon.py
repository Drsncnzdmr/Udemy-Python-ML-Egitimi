# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 00:33:32 2020

@author: Dursun Can
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix

data = pd.read_csv("veriler.csv")
x= data.iloc[:,1:4].values
y= data.iloc[:,4:].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

#Lojistik Regresyon
"""
from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred = logr.predict(X_test)
print("Tahmin Edilen",y_pred)
print("Gerçek Deper", y_test)


cm = confusion_matrix(y_test,y_pred)
print(cm)

"""

#KNN
"""
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1, metric="minkowski") #n_neighbors 1 de 6 doğru 5 de 3 doğru buldu

knn.fit(X_train,y_train)

knn_pred = knn.predict(X_test)

cm = confusion_matrix(y_test,knn_pred)
print(cm)
"""
#SVM
"""
from sklearn.svm import SVC
svc = SVC(kernel = "rbf")
svc.fit(X_train,y_train)

svc_pred = svc.predict(X_test)
cm = confusion_matrix(y_test,svc_pred)
print(cm)
"""

#Naive Bayes
"""
from sklearn.naive_bayes import GaussianNB #Bir çok yöntem var sklearn da bulunuyor.
gnb = GaussianNB()
gnb.fit(X_train, y_train)

gnb_pred = gnb.predict(X_test)
cm = confusion_matrix(y_test,gnb_pred)
print(cm)
"""

#Decision Tree
"""
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_trainq,y_train)
dt_pred = dtc.predict(X_test)
dt_cm = confusion_matrix(y_test,dt_pred)
print(dt_cm)
"""

#Random Forest
"""
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10, criterion='entropy')
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)
rfc_cm = confusion_matrix(y_test,rfc_pred)
print(rfc_cm)
"""

#Ekstra Degerlendirme
# ROC, TPR, FPR 
"""
rfc_proba = rfc.predict_proba(X_test) #Olasılıkları verir. 
print(y_test)
print(rfc_proba[:,0])

from sklearn import metrics
fpr,tpr,thold = metrics.roc_curve(y_test,rfc_proba[:,0],pos_label='e')
print('fpr',fpr) #FalsePozitiveRate
print('tpr',tpr) #TruePozitiveRate
"""


























