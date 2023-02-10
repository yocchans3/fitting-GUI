"""
参考：https://cafe-mickey.com/tag/streamlit/
"""

import streamlit as st
import numpy as np
import plotly.express as px

st.title("Streamlit test")

x = np.arange(0, 5, 0.01)
y = np.sin(x)

st.write(
    px.line(x=x, y=y, title="sin plot")
)

st.title("table test")
long_df = px.data.medals_long()
st.dataframe(long_df, width=500, height=100)



st.write("# サイドバーで選択して表とグラフをプロット")
area_list = list(long_df["nation"].unique())

#サイドバーの設定
selected_Area = st.sidebar.selectbox(
    "表示する国を選択:", 
    area_list
)

df = long_df[long_df["nation"]==selected_Area]
st.dataframe(df)
st.write(
    px.bar(df, x="medal", y="count", title="win medals : {}".format(selected_Area))
)

st.title("multi select")
long_df = px.data.medals_long()
area_list = list(long_df["nation"].unique()) #listで渡す！

selected_area = st.multiselect("select countire(s)", area_list, default="China")
df = long_df[(long_df["nation"].isin(selected_area))]


st.dataframe(df)
st.write(
    px.bar(df, x="medal", y="count", title="sample", color="nation")
)