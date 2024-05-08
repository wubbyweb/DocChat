## Core Engine
import datetime
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

class DocChat:  

    def loadvectordb(self,dbcontext):
        db_context_directory = 'db/'+dbcontext+'/'

        from langchain.vectorstores import Chroma
        from langchain.embeddings.openai import OpenAIEmbeddings
        embedding = OpenAIEmbeddings()

        self.vectordb = Chroma(
        persist_directory=db_context_directory,
        embedding_function=embedding
        )
        ##DEBUG##############################START
        __content = self.vectordb._collection.count()
        print('load.vectordb.DEBUG: '+ str(__content))
        ##DEBUG##########################################END
    
    def printvdb(self):
        print(self.vectordb._collection.count())
    
    def answer_query(self,query):

        #dotproduct = self.vectordb.similarity_search(
        #query,
        #k=4)

        current_date = datetime.datetime.now().date()
        if current_date < datetime.date(2023, 9, 2):
            llm_name = "gpt-3.5-turbo-0301"
        else:
            llm_name = "gpt-3.5-turbo"

        llm = ChatOpenAI(model_name=llm_name, temperature=0)

        # Build prompt
        template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
        {context}
        Question: {question}
        Helpful Answer:"""
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

        # Run chain
        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=self.vectordb.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )

        result = qa_chain({"query": query})

        return result['result']

