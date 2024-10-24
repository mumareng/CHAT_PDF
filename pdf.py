import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

# Maximum number of free questions
MAX_QUESTIONS = 1

# Add a section in the sidebar for the user to input the OpenAI API key
st.sidebar.header("API Key")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key (required)", type="password")

# If the OpenAI API key is provided, set it in the environment variable
if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

html_temp = f"""
 <div style="position: fixed;text-align: center; top: 0; right: 0; width: 70%; height: auto;background-color:white;  padding: 10px; border-bottom: solid 1px #e0e0e0; z-index: 1000;">
   <h1 style="text-align: center; margin-top: 30px; color: black;">
     <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIag-4EEBF1dYQ31wn5YTLj7mVZHThEJ0jvhwUdvjJTmTDXK79vSDnUdA_tyIW1tW8xbE&usqp=CAU" alt="Chat PDF" width="100" style="vertical-align: middle;"/> RAG BASED CHATPDF
   </h1>
   <p style="text-align: center; font-size: 20px; color: #3498db;">CHAT WITH PDF</p>
   <p style="text-align: center; color: black;"><a href="https://www.linkedin.com/in/muhammad-umar-farooq-85b497237/" target="_blank" style="color:  #3498db; text-decoration: none;">
    Developed by <strong>Muhammad Umar Farooq </strong>
  </a></p>
 </div>
 <div style="margin-top: 150px; margin-bottom: 15px;"> 
 </br>
 </br></br>
"""


# Close the content div at the end of your main code
st.markdown("</div>", unsafe_allow_html=True)
