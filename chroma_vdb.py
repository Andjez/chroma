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
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings

#load embedding model
#model_name = "intfloat/e5-large-v2"
#embedding = HuggingFaceEmbeddings(model_name=model_name)
embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base", model_kwargs={"device": "cpu"})

def chromadb(texts):
    vectordb = Chroma.from_documents(documents=texts, embedding=embedding)
    return vectordb
