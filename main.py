import streamlit as st
from pdfquery import PDFQuery

def extract_pdf(query):
    pdf = PDFQuery(query)
    pdf.load()
    pdf.tree.write("Puranjay.xml", pretty_print=True, encoding='utf-8')
    name = pdf.pq('LTTextLineHorizontal:in_bbox("91.112, 784.766, 185.927, 793.385")').text()
    name = name.split(' ')[0:3]
    name = ' '.join(name)

    age = pdf.pq('LTTextLineHorizontal:in_bbox("369.375, 773.439, 404.833, 782.057")').text()
    age = age.split(' ')[0:1]
    age = ''.join(age)

    gender = pdf.pq('LTTextLineHorizontal:in_bbox("370.36, 762.111, 389.519, 770.73")').text()
    gender = gender.split(' ')[0:1]
    gender = ' '.join(gender)

    hgb = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 563.789, 305.934, 572.605")').text()
    rbc_count = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 510.894, 301.032, 519.71")').text()
    tlc = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 378.658, 301.032, 387.474")').text()
    tpc = pdf.pq('LTTextLineHorizontal:in_bbox("283.877, 161.613, 298.582, 170.429")').text()
    hbA1c = pdf.pq('LTTextLineHorizontal:in_bbox("278.361, 581.322, 290.615, 590.138")').text()
    cholesterol = pdf.pq('LTTextLineHorizontal:in_bbox("272.156, 350.586, 299.114, 359.401")').text()
    glu_fasting = pdf.pq('LTTextLineHorizontal:in_bbox("272.156, 573.146, 294.213, 581.962")').text()
    return [name,age,gender,hgb,rbc_count,tlc,tpc,hbA1c,cholesterol,glu_fasting]


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
    import numpy as np
    import pandas as pd
    import pickle

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
            return df
        else:
            return df

    df = df.append(predict_admission())




        

