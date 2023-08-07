"""Streamlit is a Python library that enables fast creation of interactive web applications for machine learning and data science projects. Given our tight deadline,
 it's a great choice because it allows us to quickly build, share, and get feedback on our work without the complexities of traditional web development.
 More information can be found here: https://docs.streamlit.io/library/api-reference  https://docs.streamlit.io/library/get-started/main-concepts"""

import streamlit as st

st.title('My Summarization App')

text = st.text_input('Enter text to summarize')

if st.button('Magic'):
    st.write('Button pressed!')
