from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
load_dotenv()


loader = PyPDFLoader("./SoftwareEngineerResume.pdf")
pages = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300,chunk_overlap=100,length_function=len,add_start_index=True)
chunks = text_splitter.split_documents(pages)
print(chunks)

db = Chroma.from_documents(chunks,HuggingFaceEmbeddings(),persist_directory='./chroma_db')
query = "tell me about Jaiydevs Work Experience"
docs = db.similarity_search(query)
print(docs)