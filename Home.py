import streamlit as st
from pdfquery import PDFQuery
import numpy as np
import pandas as pd
import pickle
from pdf_extract import extract_pdf


st.set_page_config(page_title="Sarvogya", layout="wide", initial_sidebar_state="expanded")  
st.title("SARVOGYA")
st.markdown("India's first ever AI assistance to hospitals!")

report = st.file_uploader("Upload the patient's medical report:", type="pdf")
if report is not None:
    query = report
    list = extract_pdf(query)
    st.write("Name of the patient: " + list[0])
    st.write("Age of the patient: " + list[1])
    st.write("Gender of the patient: " + list[2])
    st.write("Hemoglobin level:" + list[3])
    st.write("RBC count: " + list[4])
    st.write("Total Leukocyte count: " + list[5])
    st.write("Total Platelet count: " + list[6])
    st.write("HbA1c: " + list[7])
    st.write("Cholestrol level: " + list[8])
    st.write("Glucose level: " + list[9])
    st.title("Questions from the doctor:")
    name = list[0]
    age = int(list[1])
    if list[2] == "Male":
        gender = 1
    else:
        gender = 0
    chol = list[8]
    cpt = st.text_input("Enter chest pain intensity(1-5):")
    bp = st.text_input("Enter blood pressure of the patient:")
    fbs = st.text_input("Enter whether fasting blood sugar level is above 120 of the patient:")
    ekg = st.text_input("Enter EKG results of the patient:")
    maxhr = st.text_input("Enter maximum heart rate of the patient:")
    exercise_ang = st.text_input("Enter exercise induced angina of the patient:")
    ST_dep = st.text_input("Enter ST depression of the patient:")
    ST_slope = st.text_input("Enter ST slope of the patient:")
    fluro = st.text_input("Enter number of fluro vessels patient:")
    thall = st.text_input("Enter thallium stress test results of the patient(1-10):")
    submit_button = st.button("Submit") 
else:
    st.write("OR")
    st.write("Enter the patient's details manually:")
    name = st.text_input("Enter Name of the Patient:")
    age = st.text_input("Enter Age of the Patient:")
    gender = st.text_input("Enter Gender of the patient(M/F:1/0):")
    hgb = st.text_input("Enter Hemoglobin level of the patient:")
    chol = st.text_input("Enter Cholestrol level of the patient:")
    glu = st.text_input("Enter Glucose level of the patient:")
    st.title("Questions from the doctor:")
    cpt = st.text_input("Enter chest pain intensity(1-5):")
    bp = st.text_input("Enter blood pressure of the patient:")
    fbs = st.text_input("Enter whether fasting blood sugar level is above 120 of the patient:")
    ekg = st.text_input("Enter EKG results of the patient:")
    maxhr = st.text_input("Enter maximum heart rate of the patient:")
    exercise_ang = st.text_input("Enter exercise induced angina of the patient:")
    ST_dep = st.text_input("Enter ST depression of the patient:")
    ST_slope = st.text_input("Enter ST slope of the patient:")
    fluro = st.text_input("Enter number of fluro vessels patient:")
    thall = st.text_input("Enter thallium stress test results of the patient(1-10):")
    submit_button = st.button("Submit")    


if submit_button:

    #create a dataframe to store admitted patients
    df = pd.DataFrame()

    loaded_model = pickle.load(open('model.pkl', 'rb'))
    def predict_admission():
        input = np.asarray([age,gender,cpt,bp,chol,fbs,ekg,maxhr,exercise_ang,ST_dep,ST_slope,fluro,thall])
        input = input.reshape(1, -1)
        prediction = loaded_model.predict(input)
        urgency_score = loaded_model.predict_proba(input)[:, 1]
        #change data type of urgency_score to float
        urgency_score = urgency_score.astype(float)*100
        if prediction == 1:
            st.title("Admit patient with urgency: " + str(urgency_score))
        else:
            st.title("No need to admit the patient.")
        df = pd.DataFrame()
        #append temp and urgency_score if prediction is 1
        if prediction == 1:
            input = np.append(input,urgency_score)
            input = input.reshape(1, 14)
            df = pd.DataFrame(input, columns=['Age','Gender','Chest Pain Type','Blood Pressure','Cholestrol','Fasting Blood Sugar','EKG','Max Heart Rate','Exercise Induced Angina','ST Depression','ST Slope','Fluro Vessels','Thallium Stress Test','Urgency Score'])
            # add a column for patient name at first position
            df.insert(0, "Name", name, True)
            return df
        else:
            return df


    df = df.append(predict_admission())
    #convert to json and save it to a file
    df.to_json('D:\eth-patient-list\src\data.json', orient='records')



        

