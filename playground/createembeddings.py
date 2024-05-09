import openai
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

loader = TextLoader("docs/_chat.txt",encoding='utf8')
pages = loader.load()


page = pages[0]
print(page.page_content[0:100])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150, 
    separators=["\n\n", "\n", " "]
)


docs = text_splitter.split_documents(pages)

persist_directory = 'docs/chroma/'
embedding = OpenAIEmbeddings()

vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory=persist_directory
)


vectordb.persist()