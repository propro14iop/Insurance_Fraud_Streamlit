#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:41:17 2023

@author: edwardkaiweihuang
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")



mypath = '/Users/edwardkaiweihuang/Desktop/DataScience/Insurance Fraud Detection/'
insurance_data = pd.read_csv(mypath+'insurance_data.csv')
vendor_data = pd.read_csv(mypath+'vendor_data.csv')
employee_data = pd.read_csv(mypath+'employee_data.csv')

numeric_cols = ['CLAIM_AMOUNT','PREMIUM_AMOUNT','TENURE','AGE','']  #add list of all num and cat cols here
cat_cols = ['INSURANCE_TYPE','STATE','MARITAL_STATUS','EMPLOYMENT_STATUS','RISK_SEGMENTATION','HOUSE_TYPE','SOCIAL_CLASS','CUSTOMER_EDUCATION_LEVEL','CLAIM_STATUS','INCIDENT_SEVERITY','AUTHORITY_CONTACTED','ANY_INJURY', 'POLICE_REPORT_AVAILABLE','INCIDENT_STATE','INCIDENT_HOUR_OF_THE_DAY']



insurance_data['ANY_INJURY'] = pd.Categorical(insurance_data['ANY_INJURY'],categories=[0,1])

with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation Panel',
		options = ['Abstract', 'Background Information', 'Data Cleaning','Exploratory Analysis','Data Analysis', 'Conclusion', 'Bibliography'],
		menu_icon = 'arrow-down-right-circle-fill',
		icons = ['bookmark-check', 'book', 'box', 'map', 'boxes', 'bar-chart', 
		'check2-circle'],
		default_index = 0,
		)
    
    
    
if selected=='Abstract':
    st.title('Insurance Fraud')
    
    
    



if selected=='Background Information':
    st.title('Background Information')    
    
    
    
    
    
    
if selected=='Data Cleaning':
   st.title('Data Cleaning')
      
      
      
      
   
if selected=='Exploratory Analysis':
   st.title('Exploratory Analysis')    
   col1,col2=st.columns([3,5])
   st.markdown('### Interactive Histogram')
   col1.markdown("Select numeric variables to display on histogram and choose a category column for a color.")
   with st.form("Numeric histograms"):
       x_option=col1.selectbox('Select a numeric column for the x axis',numeric_cols,key=1)
       y_option=col1.selectbox('Select a numeric column for the y axis',numeric_cols,key=2)
       color_option= col1.selectbox('Select a category variable for the color. ',cat_cols,key=3)
       nbins_input = col1.checkbox('Do you want to manually choose number of bins?')
       if nbins_input:
           
           nbins_opt = col1.number_input('Enter an interger for the number of bins.',min_value = 2)
           
       else:
           nbins_opt = None

           
       submitted=st.form_submit_button("Submit to view histogram")
       if submitted:
           fig1= px.histogram(insurance_data, x=x_option, y= y_option ,color= color_option,
             barmode= 'group',nbins= nbins_opt,histfunc= 'avg')
           col2.plotly_chart(fig1)          
    
      #everytime new graph - new name and follow format  
      
   col3,col4=st.columns([3,5])
   st.markdown('### Interactive Scatter Plot')
   col3.markdown("Select numeric variables to display on scatter and choose a category column for a color.")
            
   with st.form("Numeric Scatter plot"):
          x_option1=col3.selectbox('Select a numeric column for the x axis',numeric_cols,key=4)
          y_option1=col4.selectbox('Select a numeric column for the y axis',numeric_cols,key=5)
          color_option1= col3.selectbox('Select a category variable for the color. ',cat_cols,key=6)


              
          submitted2=st.form_submit_button("Submit to view scatter plot")
          if submitted2:
              fig2= px.scatter(insurance_data, x=x_option1, y= y_option1 ,color= color_option1,facet_col_wrap = 2 )
              col4.plotly_chart(fig2)            



   col5,col6=st.columns([3,5])
   st.markdown('### Interactive Pie-chart')
   col5.markdown("Select numeric variables to display on pie and choose a category column for a color.")
            
   with st.form("Pie Chart"):
       
          
          x_option2=col5.selectbox('Select a numeric column for the x axis',numeric_cols,key=7)
          y_option2=col5.selectbox('Select a numeric column for the y axis',cat_cols,key=8)
          color_option2= col5.selectbox('Select a category variable for the color. ',cat_cols,key=9)


              
          submitted3=st.form_submit_button("Submit to view Pie plot")
          if submitted3:
              fig3= px.pie(insurance_data, values =x_option2, names= y_option2 ,color= color_option2,hole=0.2 )
              col6.plotly_chart(fig3)               
              
              
              
   col7,col8=st.columns([3,5])
   st.markdown('### Interactive Boxplot')
   col7.markdown("Select numeric variables to display on box and choose a category column for a color.")    
   with st.form("Boxplot"):
          
          x_option3=col7.selectbox('Select a numeric column for the x axis',numeric_cols,key=10)
          y_option3=col7.selectbox('Select a numeric column for the y axis',cat_cols,key=11)
          color_option3= col7.selectbox('Select a category variable for the color. ',cat_cols,key=12)


              
          submitted4=st.form_submit_button("Submit to view boxplot")
          if submitted4:
              fig4= px.box(insurance_data,x =x_option3, y= y_option3 ,color= color_option3 )
              col8.plotly_chart(fig4)      
    
if selected=='Data Analysis':
   st.title('Data Analysis')   
   col9,col10=st.columns([3,5])
   col9.markdown('This graph is interesting because it shows that there is no difference between renting and having a mortgage.')
   fig6= px.box(insurance_data,x ='CLAIM_AMOUNT', y= 'HOUSE_TYPE' ,color= 'INSURANCE_TYPE' )
   col10.plotly_chart(fig6)   

            

if selected == "Conclusion":
    st.title('Conclusion')
    
   
 

   
if selected == 'Bibliography':
   st.title('Bibliography')
   
    




    
    
    
    
    
    