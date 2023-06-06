#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Androse_Jes
#
# Created:     05-06-2023
# Copyright:   (c) Androse_Jes 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import streamlit as st
from youtube_cap import yt_cap
from chroma_vdb import chromadb


st.title("enter your youtube link here!:smile:")
yt_link = st.text_input("valid youtube link with caption")

if yt_link:
    texts = yt_cap(yt_link)
    db = st.button(label="Generate DB")
    if db:
        vector =chromadb(texts)
        retriever = vectordb.as_retriever()
        question = st.text_input("chat with data")
        docs = retriever.get_relevant_documents(question)
        st.write(docs)

