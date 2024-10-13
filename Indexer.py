from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import redis
from redis.commands.search.field import TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
load_dotenv()
import os

VECTOR_DIMENSION = 384  # replace with your actual vector dimension

# Create a Redis client
client = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    password=os.getenv('REDIS_PASSWORD'),
    decode_responses=True
)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
if __name__ == "__main__":
        

    loader = PyPDFLoader("./SoftwareEngineerResume.pdf")
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100, length_function=len, add_start_index=True)
    chunks = text_splitter.split_documents(pages)
    pipeline = client.pipeline()

    for i, chunk in enumerate(chunks):
        embeded_value = embed_model.get_text_embedding(chunk.page_content.replace("\n", ""))
        print(len(embeded_value))
        redis_key = f"RagStore:{i:03}"
        jsonVal = {
            "embedding": embeded_value,
            "chunk": chunk.page_content,
            "metaData": {
                "source": chunk.metadata['source']
            }
        }
        # Use the set method correctly
        pipeline.json().set(redis_key, '$', jsonVal)

    # Execute the pipeline
    pipeline.execute()
