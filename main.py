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
    url = 'https://raw.githubusercontent.com/gstirk27/Z_streamlit/refs/heads/main/zelda_characters.csv'  
    response = requests.get(url)
    asdf = pd.read_csv(StringIO(response.text),header=1)
    asdf.drop(asdf.tail(1).index,inplace=True)  
    return asdf
#def get_data():
#    data = pd.read_csv('zelda_characters.csv')
#    return data

df = get_data()
#st.write(df)
df.drop(df[df['title'] == 'Freshly-Picked Tingle\'s Rosy Rupeeland'].index, inplace=True)
df.drop(df[df['race'] == ' '].index, inplace=True)

st.title("Census of Hyrule")

tab1, tab2, tab3 = st.tabs(['Main','Game','Race'])

with tab1:
    st.write("Table of Counts")
    numgames = st.number_input("Only include games that have _____ many NPCs listed",5,280)
    numraces = st.number_input("Only include races that have more than ____ entries",5,300)
    newdf = shrink_table(df,numgames,numraces)
    table = table_of_counts(newdf['race'],newdf['title'])
    st.dataframe(table)

    fig1, ax1 = plt.subplots()
    labels = newdf['race'].value_counts().index.tolist()
    ax1.pie(newdf['race'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax1.legend(labels,fontsize=5)
    ax1.set_title("Demographics (Races) of Hyrule",loc='left')
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    labels = newdf['title'].value_counts().index.tolist()
    ax2.pie(newdf['title'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax2.legend(labels,fontsize=4,loc='upper left')
    ax2.set_title("Characters in the Legend of Zelda games",loc='left')
    st.pyplot(fig2)

with tab2:
    nice = shrink_table(df,5,5)
    games = st.multiselect("Pick games to look at:", nice['title'].unique())
    gamestable = only_these_games(nice,games)
    table2 = table_of_counts(gamestable['race'],gamestable['title'])
    st.dataframe(table2)


with tab3:
    nicer = shrink_table(df,5,5)
    race = st.multiselect("Pick some fantasy races to look at:", nicer['race'].unique())
    racetable = only_these_races(nicer,race)
    table3 = table_of_counts(racetable['title'],racetable['race'])
    st.dataframe(table3)