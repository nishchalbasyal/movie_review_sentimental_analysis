import streamlit as st

from sentiments import SentimentAnalysis

movie_sentiment = SentimentAnalysis(model_path='./models/imdb_logistic_model.pkl',vectorizer_path='./models/imdb_vector.pkl')

st.header('Movie Sentiment Analysis')

review =  st.text_area('Write your Review')

choices = ['Sentiment','Probability']
user_choice = st.selectbox(label='Select One Option',options=choices)

button_clicked = st.button('Click to Compute')

if button_clicked:
    if user_choice == 'Sentiment':
        result = movie_sentiment.predict_sentiment([review])
        result = result[0]
        if result == 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Positive'

        st.text(f'This Sentiment is {sentiment} ')
    else:
        result = movie_sentiment.predict_probability([review])
        result = result[0]



        st.text(f'Negative {int(result[0] * 100)}%')
        st.text(f'Positive {int(result[1] * 100)}%')



