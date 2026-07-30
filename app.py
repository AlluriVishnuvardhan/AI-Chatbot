import streamlit as st

from utils.loader import load_pdf
from utils.splitter import split_documents

st.title("AI Knowledge Assistant")

documents = load_pdf("data/sample.pdf")

chunks = split_documents(documents)

st.write("Pages:", len(documents))
st.write("Chunks:", len(chunks))

st.subheader("First Chunk")

st.write(chunks[0].page_content)