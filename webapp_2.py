import streamlit as st
import pandas as pd
st.set_page_config(page_title="Sarvogya", layout="wide", initial_sidebar_state="expanded")  
st.title("SARVOGYA")
st.markdown("Patient Dashboard")

#read the data from the csv file
df = pd.read_csv('isAdmitted.csv',index_col=False)  
df_big = pd.read_csv('test.csv',index_col=False)
df_big.drop(['Unnamed: 0'], axis=1, inplace=True)
df.drop(['Predicted'], axis=1, inplace=True)
LOS = df_big['LOS']
df_big['LOS'] = 'TBA'
# #add a selectbox to the sidebar
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to view the data?",
#     ("As a table", "As a bar chart")
# )


#add a button to every row and give key as the index of the row
# df['Admitted'] = df.apply(lambda x: st.button('Admit', key=x), axis=1)

# add a checkbx to every row 
# df['Admitted'] = df.apply(lambda x: st.checkbox('Admit', key=x), axis=1)

# take a integer input from the user
# x = st.number_input('Enter the number of patients to be admitted', min_value=0, max_value=100, value=0, step=1)

# submit button
submit_button = st.button("Admit Patient")

# if submit button is clicked 
if submit_button:
    df_big['LOS'] = LOS

#display the data as a table
st.write(df_big)

# display buttons horizontallt in columns
# st.write(df.style.format({'Admitted': lambda x: st.button('Admit', key=x)}))



# #add a button to every row and give key as the index of the row
# df['Admitted'] = df.apply(lambda x: st.button('Admit', key=x), axis=1)

#display the data
# st.write(df)


