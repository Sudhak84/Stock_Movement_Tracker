# Python file to track the stock movement
import streamlit as st
import numpy as np
import pandas as pd
from nsepy import get_history
from datetime import datetime

# Getting the dates from the user
start=datetime(2021,1,1)
end=datetime(2021,7,30)

st.title("Stock Movement Tracker")

user_input = st.text_input("Enter the ticker here","RIL")

#st.set_page_config(layout="wide")

#Getting the stock details from the users
stock_name=[user_input]
percent_change=5.0
data=get_history(symbol=stock_name[0],start=start,end=end)
st.write(data.shape)

#Company_list=['HDFC','RELIANCE','SBIN','LT']
#len(Company_list)

#tmp_change=[]
#tmp_category=[]
#tmp=data['Prev Close'].iloc[0]
##print(tmp)
#for index,rows in data.iterrows():
#    ls_change=((rows['Close']-tmp)/tmp)
#    #print(((rows['Close']-tmp)/tmp)*100)
#    if ((rows['Close']-tmp)/tmp)*100>percent_change:
#        ls_category="Positive"
#    elif ((rows['Close']-tmp)/tmp)*100<-percent_change:
#        ls_category="Negative"
 #   else:
 #       ls_category="Neutral"
 #   #print((rows['Close']-tmp)/tmp)
 #   if abs((rows['Close']-tmp)/tmp)*100>percent_change:
 #       #print(abs((rows['Close']-tmp)/tmp)*100)
 #       tmp=rows['Close']
 #       #print(tmp)
 #   #rows['tmp_check']=
 #   tmp_change.append(ls_change)
 #   tmp_category.append(ls_category)
#data['Change%']=tmp_change
#data['Category']=tmp_category
#data.to_csv(str(stock_name[0])+'.csv')
#streamlit.dataframe(data=data, width=None, height=None)
