## Gateway web service

## Function to load vector for the chosen context

from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.append('../..')
from main import DocChat

docchat = DocChat()

app = FastAPI()

class RequestQuery(BaseModel):
    text: str

@app.post("/loadvector/")
async def process_text(request_query: RequestQuery):
    # request_query must contain the context name which is also the vector db name
    if request_query.text:
        docchat.loadvectordb(request_query.text)
        return {"message": "Text processed successfully", "processed_text": request_query.text}
    else:
        return {"message": "Invalid to context passed in does not exist"}


@app.post("/chat/")
async def process_chat(request_query: RequestQuery):
    # request_query must contain the context name which is also the vector db name
    if request_query.text:
        answer = docchat.answer_query(request_query.text)
        return {"message": answer}
    else:
        return {"message": "Invalid to context passed in does not exist"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
