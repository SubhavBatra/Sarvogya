﻿# SARVOGYA
## The entire idea can be broadly divided into three stages:
• Firstly, we have developed a machine learning model, MODEL-1 that predicts, if there is a need to admit the patient. Additionally MODEL-1 also provides with an urgency score to all new incoming patients, based on which, a priority queue can be generated to identify higher risk patients. 
• To eliminate the need of manual data entry into our model, we have developed a Data Scraper that extracts required fields from any medical report and automatically fills required inputs of the model. <br>
• Second, based on supplement and additional medical input and tests, we have developed MODEL-2, that has been ensembled to predict the LOS(Length of Stay) or Duration of Stay of every admitted patient. <br>
• Third, a mathematical algorithm that will provide the hospitals with a forecast of estimated bed management
and number of days beds will sustain if the same rate of patient admission continues. <br>
#### To ensure security and accessibility of data of all the admitted patients, the patient has been stored on ETH Blockchain (Ethereum). This has been done because LOS, primarily is a sensitive information. <br>
An effort has been made to make the usage of the models user friendly and hence, a minimalistic front-end using Streamlit has been designed.
