import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
from sklearn.model_selection import GridSearchCV
from data.getter import get_data
from analytics.plotter import plot_hist, plot_scatter, plot_outliers

if 'data' not in st.session_state:
    path = get_data()
    st.session_state['data'] = pd.read_csv(path)

if 'model' not in st.session_state:
    
    params = {'n_neighbors':np.arange(100), 'contamination':np.arange(0.1, 1, 0.1)}

    train_df = df[df.columns[5:]].copy() 

    grid = GridSearchCV(LocalOutlierFactor(), params)
    grid.fit(train_df)

    best_model = grid.best_estimator_
    y_pred = best_model.predict(train_df)

    st.session_state['model'] = best_model
    st.session_state['y_pred'] = y_pred

if 'pred_df' not in st.session_state:
    df = st.session_state['data'].copy()
    df['Outlier'] = st.session_state['y_pred']
    st.session_state['pred_df'] = df


st.markdown('# Anomaly detection of water quality with chinese dataset')
st.markdown('## With the use of Local Outlier Factor using the density of items position')

column_options = st.session_state['data'].columns.tolist()[5:]

st.markdown('## All provinces and cities')

column = st.selectbox('Choose which feature you want to visualize its outliers', column_options)

if column:
    hist_plot = plot_hist(st.session_state['data'], column)
    st.plotly_chart(plot)

    scatter_plot = plot_scatter(st.session_state['data'], province, column)
    st.plotly_chart(scatter_plot)
else:
    st.error('Choose a feature to plot')

st.markdown('## Outliers detected')
outlier_plot = plot_outliers(st.session_state['pred_df'])
st.plotly_chart(outlier_plot)

col1, col2 = st.columns(2)

province_options = st.session_state['data']['Province'].unique().tolist()

with col1:
    st.markdown('## Pick the province to analyze')
    province = st.selectbox('Choose which province you want to visualize', province_options)

with col2:
    st.markdown('## Choose which city to specialize if desired')
    df = st.session_state['data'].copy()
    city_options = ['all'] + df[df['Province'] == province].City.unique().tolist()
    city = st.selectbox('Choose which city you want to visualize', city_options)

st.markdown('## Distribution of province and cities')
spec = plot_hist(df, province, city) if city != 'all' else plot_hist(df, province)
st.plotly_chart(spec)

spec_scatter = plot_scatter(df, province, city) if city != 'all' else plot_scatter(df, province)
st.plotly_chart(spec_scatter)

st.markdown('## Outliers detected in this region')
spec_outliers = plot_outliers(df, province, city) if city != all else plot_outliers(df, province)
st.plotly_chart(spec_outliers)