import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def table_of_counts(race,title):
    tablecounts = pd.crosstab(race, title, margins=True, margins_name="Total")
    return tablecounts

def pie_chart(variable) :
    #chart = variable.value_counts().plot.pie(figsize=(7, 7), autopct='%1.1f%%')
    fig1, ax1 = plt.subplots()
    ax1.pie(variable, autopct='%1.1f%%')
    return fig1, ax1

def shrink_table(df, numgames, numraces) :
    tcg = df['title'].value_counts()
    tc1 = tcg[tcg > numgames].index
    smallerg = df[df['title'].isin(tc1)]

    tcr = df['race'].value_counts()
    tc2 = tcr[tcr > numraces].index
    smaller = smallerg[smallerg['race'].isin(tc2)]
    return smaller

def only_these_games(df,games) :
    newdf = df[df['title'].isin(games)]
    return newdf

def only_these_races(df,race) :
    newdf = df[df['race'].isin(race)]
    return newdf



