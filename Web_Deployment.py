import pickle
import sklearn
import numpy as np
import streamlit as st
import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb

from streamlit_option_menu import option_menu

stock_model_in=pickle.load(open('C:/Users/ssss/Desktop/Data Science/Deployment/Stock_Data.sav','rb'))
stock_model=pickle.load(stock_model_in)

def predict_ltp(VWAP,Delta):
    ltp_prediction=stock_model.predict([[VWAP,Delta]])
    print(ltp_prediction)
    return ltp_prediction

def main():
    st.title('Stok Prediction')
    html_temp="""
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Stock Prediction ML Model</h2>
    </div>
    """

st.markdown(unsafe_allow_html=True)
VWAP=st.text_input("VWAP","Type Here")
Delta=st.text_input("Delta","Type Here")
result=""

if st.button("Predit"):
    result=predict_ltp(VWAP,Delta)

if __name__=='__main__':
    main()

