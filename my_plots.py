import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def table_of_counts(df):
    tablecounts = pd.crosstab(df['race'], df['title'], margins=True, margins_name="Total")
    return tablecounts