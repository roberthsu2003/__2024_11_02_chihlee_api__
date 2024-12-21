import streamlit as st

#手動建立counter_key, 並設定初始值為0
if "counter" not in st.session_state:
    #st.session_state['counter'] = 0
    st.session_state.counter = 1

def increment_counter(**kwargs):
    st.session_state.counter += kwargs['first']
    st.session_state.counter -= kwargs['second']

st.header(f"這頁網頁已經執行{st.session_state.counter} 次")
st.button("再執行一次",
        key="reset",
        help='按下要加1',
        on_click=increment_counter,
        kwargs={'first':5,'second':3})#自動建立reset_key
