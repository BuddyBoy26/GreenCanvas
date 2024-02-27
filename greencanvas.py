# -*- coding: utf-8 -*-
"""
Created on Mon 26 Feb 18:21:10 2024

@author: pritv
"""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

dataog=pd.read_csv('data.csv', index_col=0, na_values=["#"])
dataoge=pd.read_csv('data.csv', index_col=0, na_values=["#"])
data=dataog.copy(deep=True)
datae=dataoge.copy(deep=False)

missing=data[data.isnull().any(axis=1)] 

#Temperature, time, Type, Combination of species, humidity, pH levels, Oxygen levels, Inflow analysis, Outflow analysis, Biological structures, filter type, UV frequency, UV intensity
#temp, time, bioreactor_type, species_combination, humidity, ph, oxygen, bio_structure, filter_type, membrane_type, uvf, uvi, 17_ALPHA_ETHINYLESTRADIOL_EE2, 17_BETA_ESTRADIOL_E2, AMIODARONE, AMISULPRIDE, AMOXICILLIN, CANDESARTAN, CARBAMAZEPINE, CLARITHROMYCIN, CIPROFLOXACIN, CYCLOPHOSPHAMIDE, DICLOFENAC, ERYTHROMYCIN, ESTRONE_E1, FENOFIBRATE, IBUPROFEN, IOHEXOL, IOVERSOL, LIDOCAINE, METOPROLOL, NAPROXEN, PARACETAMOL 

values=['temp', 'time', 'bioreactor_type', 'species_combination', 'humidity', 'ph', 'oxygen', 'bio_structure', 'filter_type', 'membrane_type', 'uvf', 'uvi', '17_ALPHA_ETHINYLESTRADIOL_EE2', '17_BETA_ESTRADIOL_E2', 'AMIODARONE', 'AMISULPRIDE', 'AMOXICILLIN', 'CANDESARTAN', 'CARBAMAZEPINE', 'CLARITHROMYCIN', 'CIPROFLOXACIN', 'CYCLOPHOSPHAMIDE', 'DICLOFENAC', 'ERYTHROMYCIN', 'ESTRONE_E1', 'FENOFIBRATE', 'IBUPROFEN', 'IOHEXOL', 'IOVERSOL', 'LIDOCAINE', 'METOPROLOL', 'NAPROXEN', 'PARACETAMOL']


def predict_rate():
    global data, datae

    new_data=pd.get_dummies(data, drop_first=True)

    features=list(set(values))

    y=new_data['rate'].values

    x = new_data[features].values

    train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)

    logistic = LogisticRegression()
    

    logistic.fit(train_x,train_y)
    logistic.coef_
    logistic.intercept_

    prediction = logistic.predict(test_x)
    #print(prediction)
    

    confusion_matrix_result = confusion_matrix(test_y, prediction)
    #print(confusion_matrix_result)
        

    accuracy = accuracy_score(test_y, prediction)
    #print(accuracy)
    

    #print('Misclassified samples: %d' % (test_y != prediction).sum())
    #print()
    #print()
    
    
    new_datae=pd.get_dummies(datae, drop_first=True)

    xe = new_datae[features].values

    print("Success Rate prediction: ")

    prediction = logistic.predict(xe)
    print(prediction)
    print(type(list(prediction)))
    print()
    print()
    
    
    return prediction

predict_rate=predict_rate()

