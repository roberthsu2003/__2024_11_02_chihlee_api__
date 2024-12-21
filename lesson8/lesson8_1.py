import streamlit as st

#手動建立counter_key, 並設定初始值為0
if "counter" not in st.session_state:
    #st.session_state['counter'] = 0
    st.session_state.counter = 0


st.header(f"這頁網頁已經執行{st.session_state.counter} 次")
buttet_status = st.button("再執行一次", key="reset")#自動建立reset_key
if buttet_status:
    st.session_state.counter += 1