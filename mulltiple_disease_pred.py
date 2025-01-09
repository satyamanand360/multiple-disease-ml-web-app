# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:14:14 2025

@author: satya_matmwh7
"""

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title="Disease ML", page_icon="https://cdn-icons-png.flaticon.com/512/3304/3304567.png")


# Attribute Information Hint for Parkinson's Disease
attribute_info = '''
### Attribute Information:

**Matrix column entries (attributes):**

- **name**: ASCII subject name and recording number
- **MDVP:Fo(Hz)**: Average vocal fundamental frequency
- **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency
- **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency
- **MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP**: Several measures of variation in fundamental frequency
- **MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA**: Several measures of variation in amplitude
- **NHR, HNR**: Two measures of ratio of noise to tonal components in the voice
- **status**: Health status of the subject (1 = Parkinson's, 0 = Healthy)
- **RPDE, D2**: Two nonlinear dynamical complexity measures
- **DFA**: Signal fractal scaling exponent
- **spread1, spread2, PPE**: Three nonlinear measures of fundamental frequency variation
'''

#loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinson_disease_model = pickle.load(open('parkinsons_model.sav','rb'))
breast_cancer_model = pickle.load(open('breast_cancer_model.sav','rb'))

# sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction',
                           'About Me'],
                           icons=['activity','heart-pulse','person-standing','lungs','info-circle'],default_index=0)
    
## Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

    
    
if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Prediction using ML')
    
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
    
    
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    st.markdown(attribute_info)

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
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_disease_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction using ML')
    
    st.markdown("""
    ### Attribute Information:
    1. ID number
    2. Diagnosis (M = malignant, B = benign)
    3-32. Ten real-valued features computed for each cell nucleus:

    - **radius**: Mean of distances from center to points on the perimeter
    - **texture**: Standard deviation of gray-scale values
    - **perimeter**: Perimeter size
    - **area**: Area size
    - **smoothness**: Local variation in radius lengths
    - **compactness**: (Perimeter^2 / area - 1.0)
    - **concavity**: Severity of concave portions of the contour
    - **concave points**: Number of concave portions of the contour
    - **symmetry**: Symmetry of the cell nucleus
    - **fractal dimension**: Coastline approximation

    The mean, standard error, and worst (mean of the three largest values) of these features were computed for each image, resulting in 30 features.
    """)

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.text_input('Mean Radius')
    with col2:
        mean_texture = st.text_input('Mean Texture')
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    with col1:
        mean_area = st.text_input('Mean Area')
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')
    with col3:
        mean_compactness = st.text_input('Mean Compactness')
    with col1:
        mean_concavity = st.text_input('Mean Concavity')
    with col2:
        mean_concave_points = st.text_input('Mean Concave Points')
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry')
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
    with col2:
        radius_error = st.text_input('Radius Error')
    with col3:
        texture_error = st.text_input('Texture Error')
    with col1:
        perimeter_error = st.text_input('Perimeter Error')
    with col2:
        area_error = st.text_input('Area Error')
    with col3:
        smoothness_error = st.text_input('Smoothness Error')
    with col1:
        compactness_error = st.text_input('Compactness Error')
    with col2:
        concavity_error = st.text_input('Concavity Error')
    with col3:
        concave_points_error = st.text_input('Concave Points Error')
    with col1:
        symmetry_error = st.text_input('Symmetry Error')
    with col2:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
    with col3:
        worst_radius = st.text_input('Worst Radius')
    with col1:
        worst_texture = st.text_input('Worst Texture')
    with col2:
        worst_perimeter = st.text_input('Worst Perimeter')
    with col3:
        worst_area = st.text_input('Worst Area')
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness')
    with col2:
        worst_compactness = st.text_input('Worst Compactness')
    with col3:
        worst_concavity = st.text_input('Worst Concavity')
    with col1:
        worst_concave_points = st.text_input('Worst Concave Points')
    with col2:
        worst_symmetry = st.text_input('Worst Symmetry')
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')

    # Code for Prediction
    cancer_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        user_input = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                      mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error,
                      texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error,
                      concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture,
                      worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity,
                      worst_concave_points, worst_symmetry, worst_fractal_dimension]

        user_input = [float(x) for x in user_input]
        user_input_as_numpy_array = np.asarray(user_input).reshape(1, -1)
        prediction = breast_cancer_model.predict(user_input_as_numpy_array)

        if prediction[0] == 0:
            cancer_diagnosis = 'The Breast Cancer is Malignant'
        else:
            cancer_diagnosis = 'The Breast Cancer is Benign'

    st.success(cancer_diagnosis)
    
if selected == 'About Me':
    st.title("About Me")
    st.write("""
    👨‍💻 **Satyam Anand**  
    📚 Machine Learning Enthusiast  
    🎓 Electrical Engineering, IIT Kharagpur  
    
    - 📧 **Email:** [satyamanand360sa@gmail.com](mailto:satyamanand360sa@gmail.com)  
    - 📧 **Alt Email:** [satyamanand@outlook.in](mailto:satyamanand@outlook.in)  
    - 🔗 **GitHub:** [github.com/satyamanand360](https://github.com/satyamanand360/)  
    - 🔗 **LinkedIn:** [linkedin.com/in/sa-satyamanand](https://www.linkedin.com/in/sa-satyamanand/)  
    """)
    
    st.write("""
    **Hello!** 👋 I'm Satyam Anand, a passionate Machine Learning enthusiast and a 3rd-year undergraduate student in Electrical Engineering at IIT Kharagpur.  
    I love exploring new technologies, building AI/ML projects, and solving real-world problems using data-driven solutions.  
    Feel free to connect with me through the links provided. Let's build something awesome together!
    """)
