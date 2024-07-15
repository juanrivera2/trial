import streamlit as st
st.title("Upload multiple files")
st.markdown("---")
files = st.file_uploader("Upload files", type= ["mp4"], accept_multiple_files=True)
if files is not None:
    for File in files:
        st.image(file)