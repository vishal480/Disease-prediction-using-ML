import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('add path for diabetes_model', 'rb'))

heart_disease_model = pickle.load(open('add path for heart_disease_model','rb'))

# sidebar for navigation

with st.sidebar:

     selected = option_menu('Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           ],
                          icons=['activity','heart',],
                          default_index=0)
    
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input da  ta from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',placeholder='0 - 10')
        
    with col2:
        Glucose = st.text_input('Glucose Level' ,placeholder='0 - 200')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value' ,placeholder='0 - 122')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value' ,placeholder='0 - 100')
    
    with col2:
        Insulin = st.text_input('Insulin Level' ,placeholder='0 - 846')
    
    with col3:
        BMI = st.text_input('BMI value' ,placeholder='0 - 67')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value' ,placeholder='0.00 - 2.40')
    
    with col2:
        Age = st.text_input('Age of the Person' ,placeholder='20 - 90')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1 ):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age',placeholder='29 - 90')
        
    with col2:
        sex = st.text_input('Gender',placeholder='Male - 1  Female - 0')
        
    with col3:
        cp = st.text_input('Chest Pain types',placeholder='0 - 3')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure',placeholder='94 - 200')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl',placeholder='126 - 564')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl',placeholder='True - 1  False - 0')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results',placeholder='0 - 2')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved',placeholder='71 - 202')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina',placeholder='Yes - 1 No - 0')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise',placeholder='0 - 6.2')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment',placeholder='0 - 2')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy',placeholder='0 - 4')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',placeholder='0 - 2')
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

#py -m streamlit run app.py
