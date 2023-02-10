"""
参考：https://cafe-mickey.com/tag/streamlit/
"""

import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import glob
from scipy.optimize import curve_fit
import plotly.graph_objects as go

## fitting関数の定義
def func(X, a, b): # １次式近似
    Y = a * np.exp(-(X-b)**2/2)
    return Y

## データ処理
datafiles = glob.glob('./data/**.csv')

data = []
for file in datafiles:
    df_ = pd.read_csv(file, header=None)
    data.append({'name':file, 'data':df_})

df_data = pd.DataFrame(data)


## 可視化
st.title("Streamlit test")

# selected_data = st.selectbox("select countire(s)", [i.get('name') for i in data])
selected_data = st.selectbox("select data", df_data['name'])


## 選択データの抜き取り
selected_data_index = df_data[df_data['name']==selected_data].index[0]
df_plot = df_data.loc[selected_data_index, 'data']
x = df_plot.iloc[:, 0].values
y = df_plot.iloc[:, 1].values


## fitting
popt, pcov = curve_fit(func, x, y) # poptは最適推定値、pcovは共分散

a = st.slider('a',  min_value=0.0, max_value=10.0, step=0.1, value=float(popt[0]))
b = st.slider('b',  min_value=-5.0, max_value=5.0, step=0.1, value=float(popt[1]))
st.write('a: {}, b: {}'.format(a, b))

plot = [
        go.Scatter(
        mode='markers',
        x=x, y=y,
        marker=dict(symbol='circle')),
        go.Scatter(
        mode='lines',
        x=x, y=func(x, a, b)),
        ]

layout = go.Layout(
    title=dict(text='{}'.format(selected_data),),
    xaxis=dict(title='x',),
    yaxis=dict(title='y',),
)
fig = go.Figure(data=plot, layout=layout)

st.write(fig)

# st.write(
#     [px.scatter(x=x, y=y, title='{}'.format(selected_data)), 
#     px.line(x=x, y=func(x, popt[0], popt[1])).update_traces(line_color='black')]
# )

st.title("table")
st.dataframe(df_plot, width=500, height=600)

