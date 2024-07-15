import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data=np.linspace(0,10,100)
#print(data)
st.sidebar.write("types of analysis")
selected_option = st.sidebar.radio("Select any plot", options=("Line","Bar","HBar"))
if selected_option=="Line":
#print(selected_option)
    st.title("Line Graph")
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(data,np.sin(data))
    plt.plot(data,np.cos(data), "--")
    st.write(fig)
elif selected_option=="Bar":
    st.title("Bar Graph")
    fig=plt.figure()
    plt.bar(data,data*10)
    st.write(fig)
else:
    st.title("Bar Horizontal")
    fig=plt.figure()
    plt.barh(data,data*10)
    st.write(fig)