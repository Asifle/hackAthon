from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from app.db import get_vector_db

openai_api_key = "your_openai_api_key"


def get_esg_response(query):
    retriever = get_vector_db().as_retriever()
    llm = OpenAI(api_key=openai_api_key)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)
