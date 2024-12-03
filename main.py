import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from io import BytesIO
from my_plots import *
import streamlit as st

#@st.cache_data
data = pd.read_csv('zelda_characters.csv')

st.title("Census of Hyrule")

tab1, tab2, tab3 = st.tabs(['Main','Game','Race'])

with tab1:
    st.write("Table of Counts")
    table = table_of_counts(data)

with tab2:
    st.write("tab2")

with tab3:
    st.write("tab3")