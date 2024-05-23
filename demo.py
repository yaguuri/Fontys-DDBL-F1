import streamlit as st

st.title("Demo Dashboard for F1 22")
st.markdown('<span style="color:Red">Apple</span>', unsafe_allow_html=True)

#Side Bar
#st.sidebar("SideBar1")

#Put Image
from PIL import Image
logo_img = Image.open("DEEPSEARCH_logo.png")
st.image(logo_img)

col1, col2 = st.columns([2,3])

with col1:
    st.title("Column1")
with col2:
    st.title("Column2")