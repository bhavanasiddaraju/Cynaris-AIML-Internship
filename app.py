from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from haystack import Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
import os

app = FastAPI(title="Haystack Dense Retrieval API")

model = SentenceTransformer("all-MiniLM-L6-v2")

pdf_data = {
    "ai.pdf": "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence. AI includes machine learning, reasoning, planning, and perception.",
    "ml.pdf": "Machine Learning is a branch of artificial intelligence where computers learn patterns from data. Common approaches include supervised learning, unsupervised learning, and reinforcement learning.",
    "deep_learning.pdf": "Deep Learning uses neural networks with multiple layers to learn complex patterns. It is widely used for image recognition, speech processing, and natural language processing.",
    "nlp.pdf": "Natural Language Processing enables computers to process and understand human language. Applications include translation, sentiment analysis, chatbots, and text classification.",
    "rag.pdf": "Retrieval Augmented Generation combines information retrieval with language generation. A retriever finds relevant documents and a language model uses the retrieved information to generate an answer."
}

documents = []

for filename, content in pdf_data.items():
    embedding = model.encode(content).tolist()

    documents.append(
        Document(
            content=content,
            meta={"file_path": filename},
            embedding=embedding
        )
    )

document_store = InMemoryDocumentStore(
    embedding_similarity_function="cosine"
)

document_store.write_documents(documents)

retriever = InMemoryEmbeddingRetriever(
    document_store=document_store,
    top_k=1
)


class QueryRequest(BaseModel):
    query: str
    top_k: int = 1


@app.get("/")
def home():
    return {
        "message": "Haystack DenseRetriever API is running"
    }


@app.post("/retrieve")
def retrieve(request: QueryRequest):
    query_embedding = model.encode(request.query).tolist()

    result = retriever.run(
        query_embedding=query_embedding,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "results": [
            {
                "source": doc.meta.get("file_path", "Unknown"),
                "content": doc.content,
                "score": doc.score
            }
            for doc in result["documents"]
        ]
    }
