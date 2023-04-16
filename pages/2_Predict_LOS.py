import pandas as pd
import streamlit as st



st.set_page_config(page_title="Sarvogya", layout="wide", initial_sidebar_state="expanded")  
st.title("SARVOGYA: Prediticting the Length of Stay (LOS) of a patient")

# add a note to the sidebar
st.sidebar.markdown("## Our trained model, utilised to predict the Length of Stay (LOS) of a patient uses 33 input features. Here are some of them and others have been fetched from the implemented dataset. \nThis is just a simulation of how certain fields can be inputted and other can be extracted from medical reports as displayed previously.") 

pid = 405
age = 50
gender = 1
smoking = st.text_input("Smoking (1/0):")
alcohol = st.text_input("Alcohol (1/0):")
htn = st.text_input("Hypertension (1/0):")
cad = st.text_input("Coronary artery disease (1/0):")
prior_cmp = st.text_input("Prior heart attack (1/0):")
hb = 15.6

tlc = st.text_input("Total Leukocyte count:")
platelet = st.text_input("Total Platelet count:")
glucose = st.text_input("Glucose level:")
rce = 0
sa = 0
a = 0
stable_ang = 0
acs = 0
st_dep = 0
atypical = 0
heart_failure = 0
valvular = 0
chb = 0
sss = 0
af = 0
vt = 0
psvt = 0
congenital = 0
ncs = 0
ortho = 0
cardio_shock = 0
shock = 0
pe = 0
chest_inf = 0

submit_button = st.button("Submit")

if submit_button:
    import numpy as np
    import pickle
    loaded_model = pickle.load(open('model_los.pkl', 'rb'))
    def predict_los():
        input = np.asarray([pid,age,gender,smoking,alcohol,htn,cad,prior_cmp,hb,tlc,platelet,glucose,rce,sa,a,stable_ang,acs,st_dep,atypical,heart_failure,valvular,chb,sss,af,vt,psvt,congenital,ncs,ortho,cardio_shock,shock,pe,chest_inf])
        input_reshaped = input.reshape(1,-1)
        prediction = loaded_model.predict(input_reshaped)
        # return prediction
        prediction = int(prediction)
        st.write("The predicted length of stay is:", str(prediction))

    predict_los()