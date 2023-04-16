import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sarvogya", layout="wide", initial_sidebar_state="expanded")  
st.title("SARVOGYA: Hospital Bed Forecasting")
#read data
df_test = pd.read_csv('bedForecast.csv')
#display data in a table and visualize it
st.markdown("## Admitted Patients sorted based on Urgency Score")
st.table(df_test)

submit_button = st.button('Forecast Bed Availability:')
if submit_button:
    totalbeds = 450
    filledbeds = 420
    #queue of urgency score and LOS only 20 rows from df_test
    new = 0
    new+=20
    queue = df_test[['Urgency Score', 'Length of Stay']].head(new).to_numpy()

    #add another column with value 0
    queue = np.insert(queue, 2, 0, axis=1)
    beds = np.zeros(450)
    #make 400 in beds 1
    for i in range(filledbeds):
        beds[i] = 1
    i+=1
    days = 1
    #create a list of days
    days_stored = []
    beds_avail = []
    while True: #real time
        st.markdown("## Day No.: " + str(days))
        days_stored.append(days)
        #decrement LOS by 1 for every patient with a bed
        for j in range(len(queue)):
            if queue[j,2] == 1:
                queue[j,1] -= 1
                #keep max of 0 or queue[j,1]
                if queue[j,1] < 0:
                    queue[j,1] = 0
                #if LOS is 0, release the bed
                if queue[j,1] == 0:
                    st.write("Released bed is: ", j+1)
                    # beds[filledbeds+j] = 0
                    i-=1
                    queue[j,2] = -1 #discharged

        st.markdown("### No. of beds available: "+str(450-i))
        beds_avail.append(450-i)
        #check if any patient does not have a bed and find the patient with highest urgency score
        while True:
            if i < 450:
                for j in range(len(queue)):
                    if queue[j,2] == 0:
                        maxi = j
                        break
                if queue[maxi,2] == 0:
                    # beds[i] = 1
                    queue[maxi,2] = 1
                    st.write("Bed filled for patient: ", maxi+1)
                    i+=1
                    #end loop if all patients are discharged
                    if np.count_nonzero(queue[:,2] == 1) + np.count_nonzero(queue[:,2] == -1) == len(queue):
                        break
            else:
                break
        st.write(" ")
        days+=1
        #select next 10 rows from df_test
        if (new > len(df_test)):
            queue_new = df_test[['Urgency Score', 'Length of Stay']].iloc[new:].to_numpy()
            queue_new = np.insert(queue_new, 2, 0, axis=1)
            queue = np.concatenate((queue, queue_new), axis=0)
            
        else:
            queue_new = df_test[['Urgency Score', 'Length of Stay']].iloc[new:new+10].to_numpy()
            queue_new = np.insert(queue_new, 2, 0, axis=1)
            queue = np.concatenate((queue, queue_new), axis=0)
            new+=10
        
        #check if queue[:,2] is all 1 or -1
        if np.count_nonzero(queue[:,2] == 1) + np.count_nonzero(queue[:,2] == -1) == len(queue):
            break
    st.title("Minimum number of days of complete hospital occupancy: "+ str(days-1))
    #plot graph of days vs beds available
    st.markdown("## Graph of Days vs Beds Available")
    #plot line chart with days_stored on x-axis and beds_avail on y-axis
    df = pd.DataFrame({'Days': days_stored, 'Beds Available': beds_avail})
    st.line_chart(df, width=0, height=0, use_container_width=True)








