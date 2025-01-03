from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize the FastAPI app
app = FastAPI()

# Initialize the text classification pipeline
text_classifier = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Define the request body structure
class TextRequest(BaseModel):
    text: str

# Define the response structure
class TextResponse(BaseModel):
    label: str
    score: float

sentiment_map = {0: "Very Negative", 1: "Negative", 2: "Neutral", 3: "Positive", 4: "Very Positive"}

@app.post("/classify", response_model=TextResponse)
def classify_text(request: TextRequest):
    try:
        # Perform text classification
        results = text_classifier(request.text)
        # Get the top result
        result = results[0]
        
        # Map the label to the sentiment_map
        label_index = int(result['label'].split('_')[-1])
        mapped_label = sentiment_map.get(label_index, "Unknown Sentiment")
        
        return TextResponse(label=mapped_label, score=result['score'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)