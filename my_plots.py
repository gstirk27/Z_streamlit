import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def table_of_counts(race,title):
    tablecounts = pd.crosstab(race, title, margins=True, margins_name="Total")
    return tablecounts

