import streamlit as st

import streamlit as st

st.title("次數的範例")
if 'count' not in st.session_state:
    st.session_state['count']=0

increament = st.button('每次加1')
if increament:
    st.session_state['count'] += 1

st.write('次數=',st.session_state['count'])
