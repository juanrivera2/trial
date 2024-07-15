import streamlit as st
import requests
from bs4 import BeautifulSoup
#st.image("https://secure.insightexpressai.com/adServer/adServerESI.aspx?script=false&amp;bannerID=11758046&amp;rnd=1720724432784&amp;redir")
with st.form("search"):
    keyword = st.text_input("Enter the keyboard")
    search = st.form_submit_button("search")
if search: 
    col1,col2,col3,col4,col5,col6 = st.columns(6)
    page_url = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    print(page_url.status_code)
    soup = BeautifulSoup(page_url.content, feature="html.parser")
    rows = soup.find_all("div",class_="d95fI")
    #print(len(rows)) - this will display the number of rows that the elemnt contains
    for row in rows:
        figures = row.find_all("figure")
        for i in range(6):
            img=figures[i].fin("img",class_="apbSI")
            list = img["srcset"].split("?")
            if i==1:
                col1.image(list[0])
            elif i==2:
                col2.image(list[0])
            elif i==3:
                col3.image(list[0])
            elif i==4:
                col4.image(list[0])
            elif i==5:
                col5.image(list[0])
            else:
                col6.image(list[0])


