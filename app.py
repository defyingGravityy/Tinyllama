import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = ("LANGCHAIN_PROJECT")

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the questiomns asked by the user."),
        ("user","{question}")
    ]
)

#streamlit 
st.title("Langchain demo with tinyllama")
input_text=st.text_input("Enter your question:")

llm = Ollama(model="tinyllama")
output_parser = StrOutputParser()
chain=prompt | llm | output_parser
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)