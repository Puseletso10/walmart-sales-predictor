import pandas as pd
import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title('Walmart Sales Predictor')

store = st.number_input('Store', min_value=1, max_value=45)
Holiday_Flag = st.selectbox('Holiday Flag', options=[0,1])
Temperature = st.number_input('Temperature', min_value=-10, max_value=50)
Fuel_Price = st.number_input('Fuel Price', min_value=0.0)
CPI = st.number_input('CPI', min_value=0.0, max_value=500.0)
Unemployment= st.number_input('Unemployment', min_value=0)

if st.button('Predict Sales'):
    input_data = pd.DataFrame({
        'Store':[store],
        'Holiday_Flag':[Holiday_Flag],
        'Temperature':[Temperature],
        'Fuel_Price':[Fuel_Price],
        'CPI':[CPI],
        'Unemployment':[Unemployment]
    })
    
    prediction = model.predict(input_data)
    st.success(f'The predicted sale for store {store} is ${prediction[0]:.2f}')