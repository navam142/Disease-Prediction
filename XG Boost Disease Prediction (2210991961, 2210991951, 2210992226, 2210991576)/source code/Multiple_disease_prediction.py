#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
import os 



# loading the saved models

diabetes_model = pickle.load(open('saved_models/diabetes_prediction.sav', 'rb'))

heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

CKD_model = pickle.load(open('saved_models/CKD_prediction.sav','rb'))

AIDS_model = pickle.load(open('saved_models/AIDS_prediction.sav','rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease prediction system using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Chronic Kidney Disease',
                            'AIDS Prediction'],
                           icons=['activity','heart','person-fill-slash','exclamation-octagon-fill','hearts'],
                           default_index= 0)
    
if(selected == 'Diabetes Prediction'):
    
    #change the page title
    st.title("Diabetes prediction")
    Pregnancies = st.text_input("Enter number of pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value ")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of Patient")
    
    
    # code for diagnosis
    diab_diag = ''
    
    #button for  prediction
    
    if(st.button("Diabetes Prediction Result")):
        diab_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,
                                             Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(diab_pred[0] == 1):
            diab_diag = 'The person is diabetic'
        else:
            diab_diag = "The person is NOT diabetic"
            
    st.success(diab_diag)

    
    

if(selected == 'Heart Disease Prediction'):
    st.title("Heart Disease prediction")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
        
    
    
    
if(selected == 'Parkinsons Disease Prediction'):
    st.title("Parkinsons Disease prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


if(selected == "Chronic Kidney Disease"):
    st.title("Chronic kidney disease model")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Age = st.text_input("Enter age")
    with col2:
        Blood_Pressure = st.text_input("BP (mm/Hg)")
    with col3:
        Specific_Gravity = st.text_input("Specific Gravity")
    with col4: 
        Albumin = st.text_input("Albumin value")
    with col5:
        Sugar = st.text_input("Sugar")

    with col1:
       Blood_Glucose_Random = st.text_input("BGR (mgs/dL)")
    with col2:
        Blood_Urea = st.text_input("Blood Urea (mgs/dL)")
    with col3:
        Serum_Creatinine = st.text_input("Serum Creatine")
    with col4:
        Sodium = st.text_input("Sodium")
    with col5:
        Potassium = st.text_input("Potassium")
    
    with col1:
        Hemoglobin = st.text_input("Hemoglobin")
    with col2:
        Packed_Cell_Volume = st.text_input("PCV")
    with col3:
        White_Blood_Cells = st.text_input("WBC")
    with col4:
        Red_Blood_Cells = st.text_input("RBC")
    with col5:
        Red_Blood_Cells_normal = st.text_input("RBC Normal")

    with col1:
        Pus_Cells_normal = st.text_input("PCN")
    with col2:
        Pus_Cell_Clumps_present = st.text_input("PCN Present")
    with col3:
        Bacteria_present = st.text_input("Bacteria present")
    with col4:
        Hypertension = st.text_input("Hypertension")
    with col5:
        Diabetes = st.text_input("Diabetes")

    with col1:
        Coronary_Artery_Disease = st.text_input("CAD")
    with col2:
        Appetite = st.text_input("Appetite")
    with col3:
        Pedal_Edema = st.text_input("Pedal Edema")
    with col4:
        Anemia = st.text_input("Anemia")
   
    CKD_diagnosis = ''

    if st.button("Predict chronic kidney disease"):

        user_input = [Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar,
       Blood_Glucose_Random, Blood_Urea, Serum_Creatinine, Sodium,
       Potassium, Hemoglobin, Packed_Cell_Volume, White_Blood_Cells,
       Red_Blood_Cells, Red_Blood_Cells_normal, Pus_Cells_normal,
       Pus_Cell_Clumps_present, Bacteria_present, Hypertension,
       Diabetes, Coronary_Artery_Disease, Appetite, Pedal_Edema,
       Anemia]


        user_input = [float(x) for x in user_input]

        CKD_prediction = CKD_model.predict([user_input])

        if CKD_prediction[0] == 1:
            CKD_diagnosis = "The person has Parkinson's disease"
        else:
            CKD_diagnosis = "The person does not have Parkinson's disease"

    st.success(CKD_diagnosis)
    
if(selected == "AIDS Prediction"):
    st.title("AIDS Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        time = st.text_input("Time")
    with col2:
        trt = st.text_input("trt")
    with col3:
        age = st.text_input("age")
    with col4: 
        wtkg = st.text_input("Weight (kg)")
    with col5:
        hemo = st.text_input("hemo")

    with col1:
       homo = st.text_input("homo")
    with col2:
        drugs = st.text_input("drugs")
    with col3:
        karnof = st.text_input("karnof")
    with col4:
        oprior = st.text_input("oprior")
    with col5:
        z30 = st.text_input("z30")
    
    with col1:
        preanti = st.text_input("preanti")
    with col2:
        race = st.text_input("race")
    with col3:
        gender = st.text_input("gender")
    with col4:
        str2 = st.text_input("str2")
    with col5:
        strat = st.text_input("strat")

    with col1:
        symptom = st.text_input("symptom")
    with col2:
        treat = st.text_input("treat")
    with col3:
        offtrt = st.text_input("offtrt")
    with col4:
        cd40 = st.text_input("cd40")
    with col5:
        cd420 = st.text_input("cd420")

    with col1:
        cd80 = st.text_input("cd80")
    with col2:
        cd820 = st.text_input("cd820")
    

    user_input = [time, trt, age, wtkg, hemo, homo, drugs, karnof,
                  oprior, z30, preanti, race, gender, str2, strat,
                  symptom, treat, offtrt, cd40, cd420, cd80, cd820]

    AIDS_diagnosis = ''

    if st.button("Predict AIDS"):

        user_input = [time, trt, age, wtkg, hemo, homo, drugs, karnof,
                  oprior, z30, preanti, race, gender, str2, strat,
                  symptom, treat, offtrt, cd40, cd420, cd80, cd820]


        user_input = [float(x) for x in user_input]

        AIDS_prediction = AIDS_model.predict([user_input])

        if AIDS_prediction[0] == 1:
            AIDS_diagnosis = "The person has AIDS"
        else:
            AIDS_diagnosis = "The person does not have AIDS"

    st.success(AIDS_diagnosis)    