import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk

# with open('linear_regression_model.pkl', 'rb') as model_file:
#    linear_regression_model = pk.load(model_file)

with open('random_forest_model.pkl', 'rb') as model_file:
   random_forest_model = pk.load(model_file)

   month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
marital_dict = {'married': 1, 'single': 2, 'divorced': 3}
poutcome_dict = {'failure': 1, 'other': 2, 'success': 3}

def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return key

def show_predict_page():
    st.title("Prediction for Term Deposit Subscription")
    st.write("### We need some information to predict the subscription")

    age = st.slider('Age', 18, 100, 18)
    duration = st.number_input("Call Duration(min)", min_value=0)
    pdays = st.number_input("Number of days that passed by after the client was last contacted from a previous campaign", min_value=-1)
    previous = st.number_input("Number of contacts performed before this campaign", min_value=0)
    balance = st.number_input('Account Balance($)', min_value=-10000)
    marital = st.selectbox("Marital Status", tuple(marital_dict.keys()))
    month = st.selectbox("Contacted Month", tuple(month_dict.keys()))
    poutcome = st.selectbox("Outcome of the last campaign", tuple(poutcome_dict.keys()))

    feature_list = [age, balance, duration, pdays, previous, get_value(marital, marital_dict), get_value(month, month_dict), get_value(poutcome, poutcome_dict)]
    single_sample = np.array(feature_list).reshape(1, -1)

    model_choice = st.selectbox("Select Model",["Random Forest Classification"])

    st.text("")

    

show_predict_page()
