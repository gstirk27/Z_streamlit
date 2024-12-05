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

with st.sidebar:
    numgames = st.number_input("Only include games that have _____ many NPCs listed",5,280)
    numraces = st.number_input("Only include races that have more than ____ entries",5,300)

tab1, tab2, tab3 = st.tabs(['Main','Game','Race'])

with tab1:
    st.subheader("Table of Counts")
    newdf = shrink_table(df,numgames,numraces)
    table = table_of_counts(newdf['race'],newdf['title'])
    st.dataframe(table)

    st.subheader("Demographics (Races) of Hyrule")
    st.write(f"These are the proportions of the different races of Hyrule amongst all the games that have more than {numgames} NPCs and {numraces} people listed as that race.")
    fig1, ax1 = plt.subplots()
    labels = newdf['race'].value_counts().index.tolist()
    ax1.pie(newdf['race'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax1.legend(labels,fontsize=5)
    st.pyplot(fig1)
 
    st.subheader("Characters in the Legend of Zelda games")
    st.write(f"These are the proportions of NPCs in each game with more than {numgames} NPCs and {numraces} in each race.")
    fig2, ax2 = plt.subplots()
    labels = newdf['title'].value_counts().index.tolist()
    ax2.pie(newdf['title'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax2.legend(labels,fontsize=4,loc='upper left')
    st.pyplot(fig2)

with tab2:
    nice = shrink_table(df,numgames,numraces)
    games = st.multiselect("Pick games to look at:", nice['title'].unique())
    gamestable = only_these_games(nice,games)
    table2 = table_of_counts(gamestable['race'],gamestable['title'])
    st.dataframe(table2)

    st.subheader("Characters in the Legend of Zelda games")
    st.write("This chart shows how many characters (of all races) feature in all the games specified above.")
    fig2, ax2 = plt.subplots()
    labels = gamestable['title'].value_counts().index.tolist()
    ax2.pie(gamestable['title'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax2.legend(labels,fontsize=4,loc='upper right')
    st.pyplot(fig2)


with tab3:
    nicer = shrink_table(df,numgames,numraces)
    race = st.multiselect("Pick some fantasy races to look at:", nicer['race'].unique())
    racetable = only_these_races(nicer,race)
    table3 = table_of_counts(racetable['title'],racetable['race'])
    st.write("If the game titles don't expand, double-click on the square to see the full name.")
    st.dataframe(table3)

    st.subheader("Demographics (Races) of Hyrule")
    st.write("This chart shows the proportion of each race selected above across all the games in the Legend of Zelda franchise.")
    fig1, ax1 = plt.subplots()
    labels = racetable['race'].value_counts().index.tolist()
    ax1.pie(racetable['race'].value_counts(),pctdistance=1.2,autopct='%1.1f%%',)
    ax1.legend(labels,fontsize=5)
    #ax1.set_title("Demographics (Races) of Hyrule",loc='left')
    st.pyplot(fig1)