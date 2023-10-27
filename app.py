import streamlit as st
import pickle as pk
from predict_page import show_predict_page
from explore_page import show_explore_page

# try:
#     from predict_page import show_predict_page
#     random_forest_model = pk.load('random_forest_model.pkl', 'rb')
# except ModuleNotFoundError:
#     print("The 'predict_page' module could not be found.")
# except FileNotFoundError:
#     print(f"The model file does not exist.")


page = st.sidebar.selectbox("Explore or Predict", ("Predict","Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()