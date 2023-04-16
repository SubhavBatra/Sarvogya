import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sarvogya", layout="wide", initial_sidebar_state="expanded")  
st.title("SARVOGYA: Patient Dashboard")

#read data
df_test = pd.read_csv('patientDashboard.csv')
df_test.drop(['Unnamed: 0'], axis=1, inplace=True)
df_test.drop(['Age'], axis=1, inplace=True)
df_test.drop(['Sex'], axis=1, inplace=True)
df_test.drop(['Predicted'], axis=1, inplace=True)
#display data in a table and visualize it
st.markdown("## Admitted Patients Details")
st.table(df_test)
