import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import matplotlib.pyplot as plt

def show_explore_page():

        st.info("Visualize Data")

        Data_Url =("BankData.csv")
        @st.cache_data(persist=True)
        def load_data():
            data  =pd.read_csv(Data_Url)
            #data['day'] = pd.to_datetime(data['day'])
            return data

        data = load_data()
    
        st.sidebar.subheader("Bank Markerting Data Analysis")

        ### Histogram & Pie chart - Analysing if customer subscribed to Fixed Deposit or not ###
        st.sidebar.markdown( "Analysing if customer subscribed to Fixed Deposit or not ")
        select3 = st.sidebar.selectbox('Visualization type', ['histogram','pie chart'],key='1')

        sentiment_count3 = data['FDcreated'].value_counts()

        sentiment_count3 = pd.DataFrame({'Bank term deposit':sentiment_count3.index, 'Count':sentiment_count3.values})

        # Reset the index of the DataFrame
        sentiment_count3 = sentiment_count3.reset_index(drop=True)

        st.title("Analysing if customer subscribed to Fixed Deposit or not")
        if select3 =="histogram":
            fig = px.bar(sentiment_count3, x='Bank term deposit' , y='Count',color='Count',height=500)
            st.plotly_chart(fig)

        else:
            fig =px.pie(sentiment_count3,values='Count',names='Bank term deposit')
            st.plotly_chart(fig)



        ### Histogram & Pie chart - Number Of People By Marital Status ###
        st.sidebar.markdown("Number Of People By Marital Status")
        select = st.sidebar.selectbox('Visualization type', ['histogram','pie chart'],key='2')

        sentiment_count = data['marital'].value_counts()

        sentiment_count = pd.DataFrame({'Marital':sentiment_count.index, 'Count':sentiment_count.values})

        st.title("Number Of customers according to Marital Status ")
        if select =="histogram":
            fig = px.bar(sentiment_count, x='Marital' , y='Count',color='Count',height=500)
            st.plotly_chart(fig) 

        else:
            fig =px.pie(sentiment_count,values='Count',names='Marital')
            st.plotly_chart(fig)



        #### Bar Chart - Number of customers according to their occupation ###
        st.title("Number of customers according to their occupation")
        job_count = data['job'].value_counts()
        job_count = pd.DataFrame({'job':job_count.index, 'Count':job_count.values})
        
        plot2 = px.bar(job_count, x='job' , y='Count',color='Count',height=500)
        st.plotly_chart(plot2)
        
        
        ### Pie chart - Number of customers having a housing loans ###
        st.title("Number of customers having a housing loans")
        housing_count = data['housing'].value_counts()
    
        housing_count = pd.DataFrame({'housing':housing_count.index, 'Count':housing_count.values})
        plot3 = px.pie(housing_count,values='Count',names='housing')
        st.plotly_chart(plot3)


        ### Pie chart - Number of customers according to education level ###
        st.title("Number of customers according to education levels")
        edu_count = data['education'].value_counts()
        #edu_count = data[data['FDcreated']== 1]['education'].value_counts()
    
        edu_count = pd.DataFrame({'education':edu_count.index, 'Count':edu_count.values})
        plot4 = px.pie(edu_count,values='Count',names='education')
        st.plotly_chart(plot4)


        selected_metrics = st.selectbox(label="Choose the feature...", options=['Duration','Campaign'])

        # Create traces
        fig = go.Figure()
        if selected_metrics == 'Duration':
            st.title("Total Call Durations By Month")

            fig.add_trace(go.Scatter(x=data.month, y=data.duration,
                        mode='markers',
                        name='duration'))


            st.plotly_chart(fig, use_container_width=True)

        #fig1 = go.Figure()
        if selected_metrics == 'Campaign':
            st.title("Total Campaigns By Month")
            fig.add_trace(go.Scatter(x=data.month, y=data.campaign,
                mode='markers', 
                name='campaign'))
        
            st.plotly_chart(fig, use_container_width=True)