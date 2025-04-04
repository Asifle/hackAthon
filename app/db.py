import pinecone

pinecone.init(api_key="your_pinecone_api_key", environment="your_pinecone_env")
index_name = "esg-data"

def get_vector_db():
    return pinecone.Index(index_name)
