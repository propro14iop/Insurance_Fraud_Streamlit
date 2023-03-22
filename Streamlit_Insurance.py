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

numeric_cols = ['CLAIM_AMOUNT','PREMIUM_AMOUNT','TENURE','AGE']  #add list of all num and cat cols here
cat_cols = ['INSURANCE_TYPE','STATE','MARITAL_STATUS','EMPLOYMENT_STATUS','RISK_SEGMENTATION','HOUSE_TYPE','SOCIAL_CLASS','CUSTOMER_EDUCATION_LEVEL','CLAIM_STATUS','INCIDENT_SEVERITY','AUTHORITY_CONTACTED','ANY_INJURY', 'POLICE_REPORT_AVAILABLE','INCIDENT_STATE','INCIDENT_HOUR_OF_THE_DAY']



insurance_data['ANY_INJURY'] = pd.Categorical(insurance_data['ANY_INJURY'],categories=[0,1])

insurance_data['INCIDENT_HOUR_OF_THE_DAY'] = pd.Categorical(insurance_data['INCIDENT_HOUR_OF_THE_DAY'],categories=np.arange(24))

insurance_data['POLICE_REPORT_AVAILABLE'] = pd.Categorical(insurance_data['POLICE_REPORT_AVAILABLE'],categories=[0,1])
insurance_data['CUSTOMER_EDUCATION_LEVEL'] = insurance_data['CUSTOMER_EDUCATION_LEVEL'].replace({np.nan:'Unknown'})

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
    st.title('Introduction to Insurance Fraud')
    st.markdown('#### By Edward Huang')
    st.markdown('Insurance fraud is a criminal offense that includes defrauding an insurance company or policyholder for financial advantage. It can manifest itself in a variety of ways, including staged incidents, bogus claims, and exaggeration of damages or injuries. Individuals, groups, and even organized crime rings can perpetrate insurance fraud.')
    st.markdown('According to fbi.gov, it is estimated that insurance fraud has steals more than 40 Billion USD annually in the United States. Many businesses have gone bankrupt from extreme cases of insurance frauds. Insurance fraud is important to prevent for several reasons. First, it can lead to higher premiums for everyone, as insurance companies pass on the costs of fraudulent claims to their customers. This means that honest policyholders end up paying more for their insurance coverage, which can be a significant financial burden.')
    st.markdown('In this personal project, I will be using my knowledge on data science to analyze datasets on insurance fraud and its cases, I will search for patterns and run models to try and predict insurance fraud. Hopefully, this can contribute to the effort of battling insurance fraud.')



if selected=='Background Information':
    st.title('Background Information')
    st.markdown('Insurance fraud is the deliberate act of tricking an insurance company into paying a claim. It is committed by people, businesses, and even networks of organized crime. According to the FBI, insurance fraud is "any act done with the purpose of obtaining a false result from an insurance process."')
    st.markdown('Insurance fraud may cost insurance companies billions of dollars annually and takes many different forms. Inflating the expense of a claim, fabricating an accident or injury to earn a claim payout, or providing false information on an insurance application are all examples of insurance fraud.')    
    st.markdown('The expenses incurred in the investigation and prosecution of the case as well as the effect on consumer rates add to the financial damage brought on by insurance fraud. Insurance fraud also damages consumer confidence and the financial stability of individuals who fall victim to it.')
    st.markdown('Insurance fraud is mostly driven by four factors: greed, retaliation, necessity, and enjoyment, according to the Coalition Against Insurance Fraud. In order to obtain money or other things, those who are motivated by greed will commit fraud. When someone decides to pursue vengeance because they believe an insurer has harmed them, revenge is a possible motivation. When someone is in need and chooses to conduct fraud in order to get money, need is a factor. The excitement of committing insurance fraud is a driving force behind organized criminal networks.')
    st.markdown('The dataset that I will use and analyze consists of ten thousand cases of insurance fraud. In each case, 38 contributing factors will be provided in the dataset to help us gain more understanding on what is going on in each insurance fraud case. These variables includes the claim amount made by the fraud, marital status, house type, employment status, tenure, age and etc. ')
    
    st.markdown('Here is what the data looks like (the warning signs are indicators for numeric data treated as categories):')
    st.dataframe(insurance_data)
    
    
if selected=='Data Cleaning':
   st.title('Data Cleaning')
   st.markdown('Data cleaning is one of the most important steps in the data analysis process. Data cleaning is the process of removing or transforming inconsistent, incomplete, or erroneous data from a dataset to make it suitable for further analysis. It can involve a variety of techniques, including data imputation, data deletion, data conversion, and data normalization.')
   
   st.markdown('Pandas and Numpy are two of the most popular Python libraries for working with data. Pandas is an open source Python library that provides easy-to-use data structures and data analysis tools. Numpy is a powerful library for scientific computing with Python that provides a number of powerful functions for working with arrays and matrices.')   
   st.markdown('Using these two libraries, data cleaning primarily focuses on dealing with missing values, incorrect values, and outliers. With Pandas, one can easily identify missing values and replace them with a suitable value. The fillna() function can be used to fill missing values with the most frequently used values in the data set. Similarly, incorrect values can be identified and replaced with the correct value, either by using the replace() function or by applying a transformation such as log transformation for normalizing the data.')
   
      
   
if selected=='Exploratory Analysis':
   st.title('Exploratory Analysis')    
   col1,col2=st.columns([3,5])
   col1.markdown('### Interactive Histogram')
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
   col3.markdown('### Interactive Scatter Plot')
   col3.markdown("Select numeric variables to display on scatter and choose a category column for a color.")
            
   with st.form("Numeric Scatter plot"):
          x_option1=col3.selectbox('Select a numeric column for the x axis',numeric_cols,key=4)
          y_option1=col3.selectbox('Select a numeric column for the y axis',numeric_cols,key=5)
          color_option1= col3.selectbox('Select a category variable for the color. ',cat_cols,key=6)


              
          submitted2=st.form_submit_button("Submit to view scatter plot")
          if submitted2:
              fig2= px.scatter(insurance_data, x=x_option1, y= y_option1 ,color= color_option1,facet_col_wrap = 2 )
              col4.plotly_chart(fig2)            



   col5,col6=st.columns([3,5])
   col5.markdown('### Interactive Pie-chart')
   col5.markdown("Select numeric variables to display on pie and choose a category column for a color.")
            
   with st.form("Pie Chart"):
       
          
          x_option2=col5.selectbox('Select a numeric column for the values. ',numeric_cols,key=7)
          
          color_option2= col5.selectbox('Select a category variable for the color. ',cat_cols,key=9)


              
          submitted3=st.form_submit_button("Submit to view Pie-plot")
          if submitted3:
              fig3= px.pie(insurance_data, values =x_option2, names= color_option2 ,color= color_option2,hole=0.2 )
              col6.plotly_chart(fig3)               
              
              
              
   col7,col8=st.columns([3,5])
   col7.markdown('### Interactive Boxplot')
   col7.markdown("Select numeric variables to display on box and choose a category column for a color.")    
   with st.form("Boxplot"):
          
          x_option3=col7.selectbox('Select a numeric column for the x axis',numeric_cols,key=10)
          y_option3=col7.selectbox('Select a categorical column for the y axis',cat_cols,key=11)
          log = col7.checkbox('Check if you want a log scale.')
 
           

              
          submitted4=st.form_submit_button("Submit to view boxplot")
          if submitted4:
              fig4= px.box(insurance_data,x =x_option3, y= y_option3 ,color= y_option3 , log_x= log)
              col8.plotly_chart(fig4)      
 
        
   st.markdown('### Interactive Sunburst') 
   col13,col14=st.columns([2,5])
   
   with st.form('Sunburst'):
       
       path_opt = col13.multiselect('Select up to 2 variables to be included inside the suburst, first selection is the inner circle.', options=cat_cols,key=13, max_selections=2)
       value_opt = col13.selectbox('Select a numeric column for the values', numeric_cols)
       submitted5 = st.form_submit_button("Submit to view Sunburst")
       if submitted5:
           
           fig11=px.sunburst(insurance_data, path=path_opt,values=value_opt, branchvalues = 'total', maxdepth = 2)
   
           col14.plotly_chart(fig11)
    
 
    
 
if selected=='Data Analysis':
   st.title('Data Analysis')   
   col9,col10=st.columns([3,5])
   col9.markdown('Keep in mind that all of the data present are all fraud cases and some of the variables inside the dataset may not at all have any relationship with determining a fraudster.')
   col9.markdown('This graph is interesting because it shows that there is no difference between renting and having a mortgage. This is pretty interesting because logically speaking, wealthier people would be less likely to be an insurance fraud while more poverished people would be portraayed more as frauds. This is because the more wealthier people normally would not need to use such vulgar ways of earning money.')
   fig6= px.box(insurance_data,x ='CLAIM_AMOUNT', y= 'HOUSE_TYPE' ,color= 'INSURANCE_TYPE' )
   col10.plotly_chart(fig6)   



    ######

   ######
   st.markdown('### Claim Amount by Incident Severity')
   col15,col16 = st.columns([1,5])
   fig12=px.histogram(insurance_data, x='CLAIM_AMOUNT', color= 'INCIDENT_SEVERITY', barmode= 'group',nbins= 10)
   
   
   
   
   col16.plotly_chart(fig12)
   
   col19,col20 = st.columns([3,5])
   col19.markdown('### Temp markdown Histogram')
   col19.markdown('In this graph, it is shown that younger people (aged around 27~37) would more likely target health insurance companies for fraud. However, health insurance frauds starts to slowly decrease in count as the age of fraudsters increases. S')
   fig12 = px.histogram(insurance_data, x='AGE', color= 'INSURANCE_TYPE', barmode= 'group',nbins= 10) 
   col20.plotly_chart(fig12)

if selected == "Conclusion":
    st.title('Conclusion')
    st.markdown('Insurance fraud is a significant problem in the insurance industry, and identifying the variables that may have a correlation to insurance fraudsters can help insurance companies better detect and prevent fraud. Some of the variables that may have a correlation to insurance fraudsters include:')
    st.markdown('Age: Studies have shown that younger people are more likely to commit insurance fraud than older individuals. This may be due to a lack of financial stability or a greater propensity for risk-taking behavior.')
    st.markdown('Occupation: Certain occupations are more likely to commit insurance fraud, such as those in the medical field, where billing fraud is a prevalent issue.')
    st.markdown('Financial distress: People who are experiencing financial distress may be more likely to commit insurance fraud in an attempt to improve their financial situation.')
    
    st.markdown('Criminal history: Individuals with a criminal history may be more likely to commit insurance fraud as they may have a higher tolerance for risk and be less concerned about the legal consequences of their actions.')
    st.markdown('Previous insurance claims: People who have a history of making excessive or fraudulent insurance claims may be more likely to continue this behavior in the future.')
    st.markdown('Lifestyle factors: Certain lifestyle factors, such as drug or alcohol addiction, may be associated with an increased risk of insurance fraud.')
    st.markdown('Geographic location: Certain geographic locations may be associated with a higher risk of insurance fraud due to factors such as the prevalence of organized crime or a lack of regulation in the insurance industry.')
    st.markdown('It is important to note that these variables do not necessarily mean that someone is committing insurance fraud. They are merely factors that may have a correlation to insurance fraudsters and can be used as part of a broader strategy to detect and prevent fraud in the insurance industry.')
   
if selected == 'Bibliography':
   st.title('Bibliography')
   st.markdown('https://content.naic.org/cipr-topics/insurance-fraud')
   st.markdown("https://www.fbi.gov/stats-services/publications/insurance-fraud")
   st.markdown('http://www.insurance.ca.gov/0300-fraud/0100-fraud-division-overview/05-ins-fraud/')
    




    
    
    
    
    
    