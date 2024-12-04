import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st
import requests
from io import StringIO

@st.cache_data
def get_data():  
    url = 'https://raw.githubusercontent.com/gstirk/Z-streamlit/main/zelda_characters.csv'  
    response = requests.get(url)
    return pd.read_csv(StringIO(response.text))  
#def get_data():
#    data = pd.read_csv('zelda_characters.csv')
#    return data

df = get_data()

st.title("Census of Hyrule")

tab1, tab2, tab3 = st.tabs(['Main','Game','Race'])

with tab1:
    st.write("Table of Counts")
    table = table_of_counts(df)
    st.dataframe(table)

with tab2:
    games = st.multiselect("Pick a Game to look at:", df['title'].unique())


with tab3:
    race = st.multiselect("Pick a fantasy race to look at:", df['race'].unique())