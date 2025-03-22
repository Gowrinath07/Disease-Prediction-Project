import streamlit as st
import pickle
import numpy as np

# Custom CSS for fresh styles
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #2193b0, #6dd5ed);
    }
    .stApp {
        background-color: #0f2027;
        padding: 20px;
        border-radius: 15px;
        color: white;
    }
    .stSidebar { 
        background-color: #16222A;
        color: white;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ff9800;
    }
    .stButton>button {
        background-color: #ff9800;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(255, 152, 0, 0.5);
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border: 2px solid #ff9800;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Parkinsons_model.sav', 'rb'))

# Sidebar navigation
st.sidebar.title('🔮 AI Disease Prediction System')
selected = st.sidebar.selectbox('🩺 Select Disease to Predict', (
    '🍩 Diabetes Test',
    '💓 Heart Health Check',
    '🧠 Parkinson’s Screening'
))

# Diabetes Prediction Page
if selected == '🍩 Diabetes Test':
    st.title('🥞 Diabetes Prediction')
    
    Pregnancies = st.number_input('🤰 Number of Pregnancies', key='pregnancies')
    Glucose = st.number_input('🍬 Glucose Level', key='glucose')
    BloodPressure = st.number_input('💖 Blood Pressure', key='blood_pressure')
    SkinThickness = st.number_input('📏 Skin Thickness', key='skin_thickness')
    Insulin = st.number_input('💉 Insulin Level', key='insulin')
    BMI = st.number_input('⚖️ BMI', format="%f", key='bmi')
    DiabetesPedigreeFunction = st.number_input('📊 Diabetes Pedigree Function', format="%f", key='dpf')
    Age = st.number_input('🎂 Age', key='age')

    if st.button('🚀 Predict Diabetes'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_prediction[0] == 1:
            st.error('🚨 High Risk of Diabetes!')
        else:
            st.success('✅ No Signs of Diabetes')

# Heart Disease Prediction Page
if selected == '💓 Heart Health Check':
    st.title('💖 Heart Disease Prediction')
    
    age = st.number_input('🎂 Age', key='heart_age')
    sex = st.number_input('⚧️ Sex (1 = Male, 0 = Female)', key='heart_sex')
    cp = st.number_input('💔 Chest Pain Type (0-3)', key='chest_pain')
    trestbps = st.number_input('💉 Resting Blood Pressure', key='rest_bp')
    chol = st.number_input('🩸 Serum Cholesterol (mg/dl)', key='cholesterol')
    fbs = st.number_input('🍬 Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)', key='fbs')
    restecg = st.number_input('📈 Resting ECG Results (0-2)', key='rest_ecg')
    thalach = st.number_input('🏃 Max Heart Rate Achieved', key='thalach')
    exang = st.number_input('🚴 Exercise Induced Angina (1 = Yes; 0 = No)', key='exang')
    oldpeak = st.number_input('📉 ST Depression by Exercise', format="%f", key='oldpeak')
    slope = st.number_input('📈 Slope of Peak Exercise ST Segment (0-2)', key='slope')
    ca = st.number_input('🩺 Major Vessels Colored (0-3)', key='ca')
    thal = st.number_input('🧬 Thalassemia (1 = Normal; 2 = Fixed Defect; 3 = Reversible Defect)', key='thal')

    if st.button('🚀 Predict Heart Health'):
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if heart_disease_prediction[0] == 1:
            st.error('🚨 Risk of Heart Disease!')
        else:
            st.success('✅ Healthy Heart!')

# Parkinson's Prediction Page
if selected == '🧠 Parkinson’s Screening':
    st.title("🎭 Parkinson's Disease Prediction")

    fo = st.number_input('🎼 MDVP:Fo(Hz)', format="%f", key='fo')
    fhi = st.number_input('🎶 MDVP:Fhi(Hz)', format="%f", key='fhi')
    flo = st.number_input('🎵 MDVP:Flo(Hz)', format="%f", key='flo')
    jitter_percent = st.number_input('📉 MDVP:Jitter(%)', format="%f", key='jitter')
    jitter_abs = st.number_input('📏 MDVP:Jitter(Abs)', format="%f", key='jitter_abs')
    rap = st.number_input('📊 MDVP:RAP', format="%f", key='rap')
    ppq = st.number_input('📈 MDVP:PPQ', format="%f", key='ppq')
    ddp = st.number_input('🔢 Jitter:DDP', format="%f", key='ddp')
    shimmer = st.number_input('✨ MDVP:Shimmer', format="%f", key='shimmer')
    shimmer_db = st.number_input('🔊 MDVP:Shimmer(dB)', format="%f", key='shimmer_db')
    
    if st.button("🚀 Predict Parkinson's"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db]])
        if parkinsons_prediction[0] == 1:
            st.error("🚨 Signs of Parkinson’s detected!")
        else:
            st.success("✅ No signs of Parkinson’s")
