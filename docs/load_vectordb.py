# Module to load vector DB
## Assumption: The vector DB contains embeddeings of the context
## Vector DB location docs/chroma

import os
import openai
import sys
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv


# set OPENAI API KEY from .env file
def load_openai_key():
    openai.api_key  = os.getenv("OPENAI_API_KEY")


def config_splitters():
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150, 
    separators=["\n\n", "\n", " "]
    )
    
def load_embeddings_module():
    embedding = OpenAIEmbeddings()

def load_vector_db():
    embedding = OpenAIEmbeddings()
    global vectordb
    vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
    )

if __name__ == '__main__':
    # add parent directory to the path to search for modules
    sys.path.append('../..')

    # read local .env file
    _ = load_dotenv(find_dotenv()) 
    load_dotenv()

    # set chroma DB location
    global persist_directory
    persist_directory = 'docs/chroma/'

    load_openai_key()
    config_splitters()
    load_embeddings_module()
    load_vector_db()

