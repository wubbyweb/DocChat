import openai
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

class CreateEmbeddings:

    def createembeddings(file_to_load,parm_chunk_size,parm_overlap_size):
        loader = TextLoader(file_to_load,encoding='utf8')
        pages = loader.load()


        page = pages[0]

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=parm_chunk_size,
            chunk_overlap=parm_overlap_size, 
            separators=["\n\n", "\n", " "]
        )

        docs = text_splitter.split_documents(pages)

        tmp_split_path = file_to_load.split("/")
        tmp_filename = tmp_split_path[len(tmp_split_path)-1].split(".")[0]
        print(tmp_filename)
        persist_directory = 'db/'+tmp_filename+'/'
        embedding = OpenAIEmbeddings()

        vectordb = Chroma.from_documents(
            documents=docs,
            embedding=embedding,
            persist_directory=persist_directory
        )

        vectordb.persist()