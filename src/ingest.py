import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()


def ingest_pdf():
    PDF_PATH = os.getenv("PDF_PATH")
    PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")
    DATABASE_URL = os.getenv("DATABASE_URL")

    documents = PyPDFLoader(PDF_PATH).load()
    split_docs = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150).split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=PG_VECTOR_COLLECTION_NAME, 
        connection=DATABASE_URL,
        use_jsonb=True
    )

    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in split_docs
    ]

    vector_store.add_documents(documents=enriched, ids=[f"doc-{i}" for i in range(len(enriched))])

if __name__ == "__main__":
    ingest_pdf()