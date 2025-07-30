import streamlit as st
import pandas as pd
import time
st.title('Hello Ritesh Welcome to the streamlit platform')

st.header('This is based on react js')

st.subheader('And we do not need any frontend knowledge for this')

st.write('This is a normal text')

st.markdown("""
### My Favorite App
- linkedin
- unstop
- whatsapp
- Nasa
""")

st.code("""
def kallu(input):
   return kallu*7

x=kallu(2)
""")

st.latex('a^3+b^3+c^3+3abc')

df=pd.DataFrame({
    'name':['Ritesh','Raju','Shyam','BabuRao'],
    'age':[19,32,31,54],
    'education':['Ug','10','Pg','5']

})

st.dataframe(df)

st.metric('Revenue','Rs 7L','-3%')

st.json({
    'name':['Ritesh','Raju','Shyam','BabuRao'],
    'age':[19,32,31,54],
    'education':['Ug','10','Pg','5']
})

st.image('nature.jpg')

st.sidebar.title('sidebar ka title hai ye')

col1,col2=st.columns(2)

with col1:
    st.image('nature.jpg')

with col2:
    st.image('nature.jpg')


st.error('login failed')

st.success('login success')

bar=st.progress(0)

for i in range(1,101):
    bar.progress(i)


email=st.text_input('Enter your email')
num=st.number_input('Enter your age')
date=st.date_input('Enter your admisson date')

file=st.file_uploader('Upload a csv file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())
