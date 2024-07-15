import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

data=np.linspace(0,10,100)
#print(data)
st.sidebar.write("types of analysis")
selected_option = st.sidebar.radio("Select any plot", options=("Line","Bar","HBar"))
if selected_option=="Line":
#print(selected_option)
    fig=plt.figure()
    plt.plot(data,np.sin(data))
    plt.plot(data,np.cos(data), "--")
    st.write(fig)
elif selected_option=="Bar":
    fig=plt.figure()
    plt.bar(data,data*10)
    st.write(fig)
else:
    fig=plt.figure()
    plt.bar(data,data*10)
    st.write(fig)