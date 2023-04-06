import pandas as pd
import streamlit as st
from helper_functions import *

st.title('Custom Air Quality Index Calculator')

st.header('Parameters')

st.markdown('Need atleast **:red[3]** readings inorder to calculate AQI.')
st.markdown('Either **:red[PM10]** or **:red[PM2.5]** is compulsory.')

with st.container():
    left_column, right_column = st.columns(2)
    
    with left_column:
        
        PM10 = st.number_input('PM10', min_value = 0, value = 121)
        SO2 = st.number_input('SO2', min_value = 0, value = 0)
        CO = st.number_input('CO', min_value = 0, value = 0)
        NH3 = st.number_input('NH3', min_value = 0, value = 34)

    with right_column:
        
        PM25 = st.number_input('PM2.5', min_value = 0, value = 34)
        NOx = st.number_input('NOx', min_value = 0, value = 8)
        O3 = st.number_input('O3', min_value = 0, value = 57)
        
dataFrame = pd.DataFrame({'PM10_sub_idx' : [round(get_PM10_Sub_Index(PM10), 0)],
                          'PM2.5_sub_idx' : [round(get_PM25_Sub_Index(PM25), 0)],
                          'SO2_sub_idx' : [round(get_SO2_Sub_Index(SO2), 0)],
                          'NOx_sub_idx' : [round(get_NOx_Sub_Index(NOx), 0)],
                          'CO_sub_idx' : [round(get_CO_Sub_Index(CO), 0)],
                          'O3_sub_idx' : [round(get_O3_Sub_Index(O3), 0)],
                          'NH3_sub_idx' : [round(get_NH3_Sub_Index(NH3), 0)]})

# st.dataframe(dataFrame)

dataFrame['Check'] = (dataFrame['PM10_sub_idx'] > 0).astype(int) + \
                     (dataFrame['PM2.5_sub_idx'] > 0).astype(int) + \
                     (dataFrame['SO2_sub_idx'] > 0).astype(int) + \
                     (dataFrame['NOx_sub_idx'] > 0).astype(int) + \
                     (dataFrame['CO_sub_idx'] > 0).astype(int) + \
                     (dataFrame['O3_sub_idx'] > 0).astype(int) + \
                     (dataFrame['NH3_sub_idx'] > 0).astype(int)

# st.dataframe(dataFrame)

st.header('AQI Value')

col1, col2, col3 = st.columns(3)
if dataFrame.loc[0, 'PM10_sub_idx'] + dataFrame.loc[0, 'PM2.5_sub_idx'] > 0 and dataFrame.loc[0, 'Check'] >= 3:
    col2.success(dataFrame.iloc[0].max())
else:
    col2.error('Atleast 3 inputs needed\n\nNeed atleast **PM10** OR **PM2.5** value')