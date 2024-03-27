# Module to load vector DB
## Assumption: The vector DB contains embeddeings of the context
## Vector DB location docs/chroma

import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv


    
def load_vector_db(chroma_directory):
    embedding = OpenAIEmbeddings()
    vectordb = Chroma(
    persist_directory=chroma_directory,
    embedding_function=embedding
    )
    ##DEBUG##############################START
    __content = vectordb._collection.count()
    print('load.vectordb.DEBUG: '+ str(__content))
    ##DEBUG##########################################END

    return vectordb

if __name__ == '__main__':
    # read local .env file
    _ = load_dotenv(find_dotenv()) 
    load_dotenv()

    # set chroma DB location
    chroma_directory = os.getenv('CHROMA_LOC_DFT')

    vector_db_content = load_vector_db(chroma_directory)
    
    print(vector_db_content._collection.count())



