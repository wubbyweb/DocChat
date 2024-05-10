# DocChat
SaaS application enables chat with document.  There are several such applications available out there... Its my own piece to understand the concepts

The application uses RAG based architecture to create vector embeddings for the document uploaded to the application and allows users to chat with the document. 

## playground
The folder has several python scripts and jupyter notebooks, helpful if you are pursuing a step by step replication of the solution

## Server run
uvicorn run:app --reload

## Deployment

The application is deployed as microservice at endpoint https://docchat-u6rh.onrender.com  (Render.com)
POST request to the above url at port 8000.  (Note, the application runs under free tier and therefore first time request may be delayed upto 50 seconds)

## Frontend 

The application frontend project is DocChat-web https://github.com/wubbyweb/DocChat-web.git 

