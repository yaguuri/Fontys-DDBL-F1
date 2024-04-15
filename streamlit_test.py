import streamlit as st

#Side Bar
#st.sidebar("SideBar1")

#Put Image
#from PIL import Image
#logo_img = Image.open("C:/Users/lys17/Desktop/DEEPSEARCH_logo.png")

#Initialize connection
conn = st.connection("mysql", type="sql")

#perform query
#ttl=600: to ensure the query result is cached for no longer than 10 minutes
df = conn.query("SELECT * FROM mytable;", ttl=600)
    
#print result
st.table(df.head())