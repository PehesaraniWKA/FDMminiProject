import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk

# with open('linear_regression_model.pkl', 'rb') as model_file:
#    linear_regression_model = pk.load(model_file)

with open('random_forest_model.pkl', 'rb') as model_file:
   random_forest_model = pk.load(model_file)