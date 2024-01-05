import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.title('Crab Age Prediction :crab: ')

sex_mapping = {
    'Male': 2,
    'Female': 0,
    'Unknown': 1,
    None: 0,
}

option = st.radio(
    "Crab Sex",
    ["Male", "Female", "Unknown"],
    index=None,
)
selected_option = sex_mapping[option]

Length = st.number_input('Length', min_value=0.0, max_value=3.0, step=1e-5,format="%.5f")
Diameter = st.number_input('Diameter', min_value=0.0, max_value=2.0, step=1e-5,format="%.5f")
Height = st.number_input('Height', min_value=0.0, max_value=3.0, step=1e-5,format="%.5f")
Weight = st.number_input('Weight', min_value=0.0, max_value=100.0, step=1e-5,format="%.5f")
Shucked_Weight = st.number_input('Shucked Weight', min_value=0.0, max_value=50.0, step=1e-5,format="%.5f")
Viscera_Weight	 = st.number_input('Viscera Weight', min_value=0.0, max_value=30.0, step=1e-5,format="%.5f")
Shell_Weight = st.number_input('Shell Weight', min_value=0.0, max_value=40.0, step=1e-5,format="%.5f")

with open('XGB_submission.pkl', 'rb') as file:
    model = pickle.load(file)

if st.button('Predicted Crab Age'):
    input_data = np.array([selected_option ,Length, Diameter, Height, Weight, Shucked_Weight,Viscera_Weight, Shell_Weight]).reshape(1, -1)

    prediction = model.predict(input_data)
    show_predict = int(round(prediction[0],0))
    st.success(f'Predicted Crab Age: {show_predict}')
    if(show_predict <= 6):
        image = Image.open('CrabChild_Ai.jpg')
        st.image(image, caption="I'm a child crab")
    elif(7 <= show_predict and show_predict <= 12):
        image = Image.open('Teen_Crab.jpg')
        st.image(image, caption="I'm a teen crab")
    else:
        image = Image.open('Old_Crab.jpg')
        st.image(image, caption="I'm a Old crab")

    st.balloons()