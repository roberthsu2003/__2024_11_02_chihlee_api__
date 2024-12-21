from tools import fetch_youbike_data
import streamlit as st

youbike_data:list[dict] = fetch_youbike_data()

# 使用streamlit分2個欄位
# 使用you_bike_data:list的資料, 取出所有的行政區域(sarea), 不可以重複
# 左邊是選擇行政區域(sarea), 使用下拉式表單
# 右邊是顯示該行政區域的YouBike站點資訊的表格資料
# 最下方是顯示該行政區域的YouBike站點資訊的地
area_list = list(set(map(lambda value:value['sarea'],youbike_data)))
col1,col2 = st.columns([1,3])
with col1:
   selected_area = st.selectbox("行政區域",area_list)
   

with col2:
    def filter_func(value:dict)->bool:
        return value['sarea'] == selected_area
        
    filter_list:list[dict] = list(filter(filter_func,youbike_data))
    show_data:list[dict] = [{
                            '站點':item['sna'],
                            '總車輛數':item['tot'],
                            '可借車輛數':item['sbi'],
                            '可還空位數':item['bemp'],
                            '營業中':item['act'],
                            'latitute':item['lat'],
                            'longitute':item['lng']
                             } for item in filter_list]
    st.dataframe(show_data)


# with col2:
#     filter_data = filter(lambda item:item['sarea'] == selected_sarea,youbike_data)
#     st.dataframe(filter_data)

# #顯示地圖
# filter_data = list(filter(lambda item:item['sarea'] == selected_sarea,youbike_data))
# locations = [{'lat': float(item['lat']), 'lon': float(item['lng'])} for item in filter_data]
# st.map(locations)