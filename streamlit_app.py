import streamlit as st
st.write('Hello world!!')

st.header('st.button')
if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Good bye')