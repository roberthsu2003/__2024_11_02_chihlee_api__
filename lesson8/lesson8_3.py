from tools import fetch_youbike_data
import streamlit as st
import pandas as pd

youbike_data:list[dict] = fetch_youbike_data()

# 使用streamlit分2個欄位
# 使用youbike_data:list的資料,取出所有的行政區域(sarea),不可以重複
# 左邊是選擇行政區域(sarea),使用下拉式表單
# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
# 最下方是顯示該行政區域的YouBike站點資訊的地圖
sarea_list = sorted(list(set([station['sarea'] for station in youbike_data])))
col1, col2 = st.columns(2)

with col1:
    selected_sarea = st.selectbox("選擇行政區域", sarea_list)
with col2:
    filter_data = [station for station in youbike_data if station['sarea'] == selected_sarea]
    print(filter_data)
    st.dataframe(pd.DataFrame(filter_data))

st.map(data=filter_data, latitude='lat', longitude='lng')
st.map(data=filter_data, latitude='lat', longitude='lng')