from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()

st.header('Research Tool')

user_input = st.text_input('Enter you prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.com)