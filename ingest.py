from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
from src.helper import load_pdf, text_split, download_hugging_face_embeddings



extracted_data = load_pdf("data/") 

text_chunks = text_split(extracted_data) 

embeddings = download_hugging_face_embeddings()


url = "http://localhost:6333"
qdrant = Qdrant.from_documents(
    text_chunks,
    embeddings,
    url=url,
    prefer_grpc=False,
    collection_name="vector_db"
)
print("Vector DB Successfully Created!")