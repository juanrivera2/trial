import streamlit as st
st.markdown("<h1 style = "text-align: center"> User registration form </h1>",unsafe_allow_html=True)
with st.form("form1", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First name")
    l_name = col1.text_input("Last name")
    st.text_input("Enter email")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    st.form_submit_button("Submit")
    submit_state= st.form_submit_button("Submit")
    if submit_state:
        if f_name == "" and l_name =="":
            st.warning("Please fill above fields")
        else:
            st.success("Submitted successfully")
