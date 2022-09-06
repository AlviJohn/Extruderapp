import streamlit as st
import numpy as np
import pandas as pd
from chart_studio import plotly as py
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from itertools import product
from PIL import Image


#######Setting the Basics for the Page
st.set_page_config(page_title="Extrusion App", page_icon="muscleman.jpg", layout="wide", initial_sidebar_state="auto")
st.title('Extrusion App')


Raw_data = pd.read_csv('Raw_data.csv',encoding="cp1252") 








###########################################Filtering Option#########################################
st.sidebar.title('Dashboard Filters')



###########Selecting Cavity

Workorder_choices = Raw_data['order_id'].unique().tolist()

Workorder_choices_V2 =Workorder_choices
Workorder_choices_V2.insert(0,"ALL")

make_choice = st.sidebar.multiselect("Select one or more Extrusion Work Orders:",Workorder_choices_V2,'ALL')

if "ALL" in make_choice:
    Workorder_make_choice_final = Workorder_choices_V2
else:
    Workorder_make_choice_final  = make_choice





Raw_data=Raw_data.loc[Raw_data['order_id'].isin(Workorder_make_choice_final),:]



option = st.selectbox('Please select Variable of Interest',Raw_data.columns)

###########Charts#########################
fig = go.Figure()
fig = px.scatter(Raw_data,x='PCRQPLX_A_takeaway_speed', y=option, color='Status')
fig.update_layout(title_text= "Change in " + option + " during Pushout/Rampup/Stable Time Period")
st.plotly_chart(fig,use_container_width=True)


if make_choice != "ALL":
    fig = go.Figure()
    fig = px.scatter(Raw_data,x='start_time', y=option, color='Status')
    fig.update_layout(title_text= "Change in " + option + " during Pushout/Rampup/Stable Time Period")
    st.plotly_chart(fig,use_container_width=True)



#TD_Width_dataset = pd.read_csv('Combined_data_V1.csv',encoding="cp1252") 
#
#option = st.selectbox('Please select the SKU',TD_Width_dataset['ct_code'].unique())
#
#TD_subset = TD_Width_dataset.loc[TD_Width_dataset['ct_code']==option ,:]
#
##TD_subset = TD_Width_dataset
#
#p_001=TD_subset['TD Width Variation'].quantile(0.001)
#p_995= TD_subset['TD Width Variation'].quantile(0.995)
#TD_subset['TD Width Variation'].clip(lower=p_001, upper=p_995, inplace=True)
#
#TD_subset['Spec Details'] = TD_subset['TD Width Variation'].apply(lambda x:'Outside Threshold' if x<=-2 else 'Within Spec')
#
#st.write(TD_subset.groupby(['Spec Details']).\
#    agg({'Rejected Tyres': ['mean'],
#        'BARCODE': ['count']}).reset_index())
#
###########Charts#########################
#var = option
#
#fig = go.Figure()
#fig = px.violin(TD_subset, y='TD Width Variation',color="Rejected Tyres" ,box=True)
#fig.update_layout(title_text= "Rejected Tyres")
#st.plotly_chart(fig,use_container_width=True)




