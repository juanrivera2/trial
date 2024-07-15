import streamlit as st
import requests
from bs4 import BeautifulSoup
#st.image("https://plus.unsplash.com/premium_photo-1668110864450-48a6591c3a22")
with st.form("Search"):
    keyword=st.text_input("Enter the keyword")
    search= st.form_submit_button("Search")
if search:
    col1,col2,col3=st.columns(3)
    page_url=requests.get(f'https://unsplash.com/s/photos/{keyword}')
    #print(page_url.status_code)
    soup=BeautifulSoup(page_url.content,features="html.parser")
    rows=soup.find_all("div",class_='d95fI')
    print(len(rows))
    #O9fwi
    for row in rows:
        figures = row.find_all("figure")
        for i in range(3):
            img=figures[i].find("img",class_="ApbSI")
            list=img["srcset"].split("?")
            if i==1:
                col1.image(list[0])
            elif i==2:
                col2.image(list[0])
            else:
                col3.image(list[0])
            #print("\n\n")