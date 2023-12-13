import streamlit as st
import joblib

class SentimentAnalysis:
    def __init__(self,model_path,vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict_sentiment(self,sentences):
        sentences = self.vectorizer.transform(sentences)
        pred = self.model.predict(sentences)
        return pred
    
    def predict_probability(self,sentences):
        sentences = self.vectorizer.transform(sentences)
        probability = self.model.predict_proba(sentences)
        return probability
    