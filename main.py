import streamlit as st

st.header('ML Deployment')

st.subheader('This is a Sub header')

st.text('We are deploying our ML project here')

text_data = st.text_input('Enter your message here')

st.write(text_data)


age = st.number_input('Enter Age',min_value=0,max_value=100)
st.write(age)

age = st.slider('Select Age',min_value=0,max_value=100,step=1)

button = st.button('Click Me')

st.write(f'Button Clicked: {button}')

date = st.date_input('Start Date')

drinks = ['Whisky','Beer','Rum','local','Vodka','Chhyang','Toongba','Tari','Wine']

user_selected = st.radio('Select One',options=drinks)


drop_down = st.selectbox('Select one',options=drinks)

multi_select = st.multiselect('Select as much as you can drink',options=drinks)

