import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk

# with open('linear_regression_model.pkl', 'rb') as model_file:
#    linear_regression_model = pk.load(model_file)

with open('random_forest_model.pkl', 'rb') as model_file:
   random_forest_model = pk.load(model_file)

marital_dict = {'married': 1, 'single': 2, 'divorced': 3}
poutcome_dict = {'failure': 1, 'other': 2, 'success': 3}
job_dict = {'admin.': 0, 'services': 1, 'management': 2, 'blue-collar': 3, 'technician': 4, 'unemployed': 5, 'entrepreneur': 6, 'housemaid': 7, 'retired': 8, 'self-employed': 9, 'student': 10}
# month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}


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
    # pdays = st.number_input("Number of days that passed by after the client was last contacted from a previous campaign", min_value=-1)
    previous = st.number_input("Number of contacts performed before this campaign", min_value=0)
    balance = st.number_input('Account Balance($)', min_value=-10000)
    marital = st.selectbox("Marital Status", tuple(marital_dict.keys()))
    job = st.selectbox("Job", tuple(job_dict.keys()))
    poutcome = st.selectbox("Outcome of the last campaign", tuple(poutcome_dict.keys()))

    feature_list = [age, balance, duration, previous, get_value(marital, marital_dict), get_value(job, job_dict), get_value(poutcome, poutcome_dict)]
    single_sample = np.array(feature_list).reshape(1, -1)

    model_choice = st.selectbox("Select Model",["Random Forest Classification"])

    st.text("")

    if st.button("Predict"):
        if model_choice == "Random Forest Classification":
            prediction = random_forest_model.predict(single_sample)
            pred_prob = random_forest_model.predict_proba(single_sample)

            if prediction == 0:
                st.text("")
                st.warning("Customer doesn't create Bank Term Deposit")
                pred_probability_score = {"Not creating account":pred_prob[0][0]*100,"Creating Account":pred_prob[0][1]*100}
                #st.markdown(result_temp,unsafe_allow_html=True)
                st.text("")
                st.subheader("Prediction Probability Score using {}".format(model_choice))
                st.info(pred_probability_score)			
            else:
                st.text("")
                st.success("Customer creates Bank Term Deposit")
                pred_probability_scoreY = {"Not creating account":pred_prob[0][0]*100,"Creating Account":pred_prob[0][1]*100}
                #st.markdown(result_temp,unsafe_allow_html=True)
                st.text("")
                st.subheader("Prediction Probability Score using {}".format(model_choice))
                st.json(pred_probability_scoreY)

show_predict_page()
