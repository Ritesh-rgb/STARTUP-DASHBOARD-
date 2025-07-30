import streamlit as st

email=st.text_input('Enter your email')

password=st.text_input('Enter your password')

gender=st.selectbox('select gender',['Male','Female','Others'])

btn=st.button('login karo')

if btn:
    if email== 'riteshthala432@gmail.com' and password=='password':
        st.success('Loginned Successfully')
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')




