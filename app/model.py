import joblib
from transformers import pipeline

MODEL_PATH = "model/sentiment_model.pkl"

def load_model():
    return pipeline("sentiment-analysis")

def predict_sentiment(model, text: str):
    result = model(text)
    return result[0]['label']