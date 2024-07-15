import streamlit as st
st.title("Upload multimedia files")
st.markdown("---")
file = st.file_uploader("please upload an sudio file", type= ["mp4"])
if file is not None:
    st.image(file)
    st.audio(file)
    st.video(file)
