import streamlit as st

#Side Bar
#st.sidebar("SideBar1")

#Put Image
from PIL import Image

logo_img = Image.open("C:/Users/lys17/Desktop/DEEPSEARCH_logo.png")

#Columns
col1, col2 = st.columns([2,3]) #split space into 2:3

#contents of col1
with col1:
    st.title("column1")

#contents of col2
with col2:
    st.title("column2")
    st.checkbox("checkbox1 in col2")
    st.checkbox("checkbox2 in col2")


#Tab
tab1, tab2 = st.tabs(["Tab A", "Tab B"])

with tab1:
    st.write("Here is the Tab 1")

with tab2:
    st.write("Here is the Tab 2")