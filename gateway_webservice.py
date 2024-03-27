## Gateway web service

## Function to load vector for the chosen context

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestQuery(BaseModel):
    text: str

@app.post("/loadvector/")
async def process_text(input_text: RequestQuery):
    # Here you can add your text processing logic
    processed_text = input_text.text.upper()  # Example: Convert text to uppercase

    # Check if the processed text meets some criteria
    if processed_text:
        return {"message": "Text processed successfully", "processed_text": processed_text}
    else:
        return {"message": "Error processing text"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
