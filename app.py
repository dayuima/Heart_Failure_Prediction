import streamlit as st
import pandas as pd
import numpy as np
import joblib

with open('model_rfc.pkl','rb') as file_1:
  model_rfc = joblib.load(file_1)

with open('model_ada.pkl','rb') as file_2:
  model_ada = joblib.load(file_2)

st.title('Heart Prediction')


usia = st.slider('Usia', min_value = 40, max_value = 95, value = 45)
st.write('Masukkan Usia Anda:', usia)

injeksi_freksi = st.slider('Ejection Fraction',min_value = 14, max_value = 80, value = 17)
st.write('Masukkan Injeksi Freksi Anda:', injeksi_freksi)

high_blood_pressure = st.slider('High Blood Pressure',min_value = 0, max_value = 1, value = 0)
st.write('Masukkan High Blood Pressure Anda:', high_blood_pressure)

serum_creatinine = st.slider('Serum Creatinine', min_value = 0.5, max_value = 9.4, value = 1.6)
st.write('Masukkan Serum Creatinine Anda :', serum_creatinine)

serum_sodium = st.slider('Serum Sodium', min_value = 113, max_value = 148, value = 120)
st.write('Masukkan Serum Sodium Anda:', serum_sodium)

df_inf = pd.DataFrame({
    'age' : [usia],
    'ejection_fraction' : [injeksi_freksi],
    'high_blood_pressure': [high_blood_pressure],
    'serum_creatinine': [serum_creatinine],
    'serum_sodium': [serum_sodium]
})

model_rfc1 = model_rfc.predict(df_inf[['age','ejection_fraction','high_blood_pressure','serum_creatinine','serum_sodium']])

if st.button('Predict'): 
    final_result_rfc = model_rfc.predict(df_inf[['age','ejection_fraction','high_blood_pressure','serum_creatinine','serum_sodium']])
    st.write('Hasil Prediksi: ')
    if final_result_rfc == 1:
        st.subheader('Gagal Jantung')
    else:
        st.subheader('Tidak gagal jantung')


