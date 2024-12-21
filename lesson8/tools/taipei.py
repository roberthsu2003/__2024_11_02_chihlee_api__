import requests
from requests import Response
from io import StringIO
from csv import DictReader
from requests.exceptions import RequestException, HTTPError
import streamlit as st


@st.cache_data
def fetch_youbike_data() -> list[dict]:
    """
    從新北市資料開放平台獲取YouBike站點資訊
    
    Returns:
        list[dict]: 包含所有YouBike站點資訊的字典列表
    """
    api_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        response: Response = requests.request('GET', api_url)
        response.raise_for_status()   
    except HTTPError:
        raise Exception("無法連接到資料伺服器，請稍後再試")
    except RequestException:
        raise Exception("網路連線異常，請檢查網路設定")
    else:
        print("資料下載成功")
        csv_file = StringIO(response.text)
        csv_reader = DictReader(csv_file)
        bike_stations: list[dict] = list(csv_reader)
        return bike_stations