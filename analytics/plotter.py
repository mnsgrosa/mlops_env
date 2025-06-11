import plotly.express as px
import pandas as pd

def plot_hist(df, column, province = None, city = None):
    temp = df.copy()
    if province:
        temp = temp[(temp['City'] == city) & (temp['Province'] == province)] if city else temp[temp['Province'] == province]
    fig = px.histogram(temp, x = column)
    return fig

def plot_scatter(df, province, column, city = None):
    temp = df.copy()
    if province:
        temp = temp[(temp['City'] == city) & (temp['Province'] == province)] if city else temp[temp['Province'] == province]
    fig = px.scatter(temp, x = 'Latitude', y = 'Longitude', color = column)
    return fig

def plot_outliers(df, province = None, city = None):
    temp = df.copy()
    if province:
        temp = temp[(temp['City'] == city) & (temp['Province'] == province)] if city else temp[temp['Province'] == province]
    fig = px.scatter(temp, x = 'Latitude', y = 'Longitude', color = 'Outlier')
    return fig