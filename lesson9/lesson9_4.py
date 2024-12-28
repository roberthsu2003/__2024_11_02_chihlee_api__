import streamlit as st

st.title('1元1次方程式')
st.title('Y = 2X - 1')

prompt = st.chat_input("請輸入X的值:")
if prompt:
    st.write(prompt)