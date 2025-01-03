from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import load_model, predict_sentiment

app = FastAPI()
model = load_model()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    try:
        result = predict_sentiment(model, input.text)
        return {"sentiment": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))