import pickle
from typing import List
import faiss
import numpy as np
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from src.config import FAISS_INDEX_FILE, METADATA_FILE
from src.embeddings.embeddings_manager import EmbeddingsManager
from src.data.loader import CorpusLoader
from src.data.preprocessor import TextPreprocessor
from src.utils.logger import get_logger


logger = get_logger(__name__)

class HuggingFaceEmbeddings(Embeddings):
    def __init__(self, manager: EmbeddingsManager):
        self.manager = manager

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.manager.embed_texts(texts).tolist()

    def embed_query(self, text: str) -> List[float]:
        return self.manager.embed_text(text).tolist()

class VectorStoreManager:
    def __init__(self):
        self.vectorstore = None
        self.embeddings_manager = EmbeddingsManager()
        self.embeddings = HuggingFaceEmbeddings(self.embeddings_manager)
    
    def create_vectorstore(self, documents: List[Document]) -> FAISS:
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        logger.info(f"Created vectorstore with {len(documents)} documents")
        return self.vectorstore

    def save_vectorstore(self, filepath: str = str(FAISS_INDEX_FILE.parent)):
        if self.vectorstore is None:
            logger.error("Vectorstore is not initialized. Cannot save.")
            return

        self.vectorstore.save_local(filepath)

    def load_vectorstore(self, filepath: str = str(FAISS_INDEX_FILE.parent)) -> FAISS:
        self.vectorstore = FAISS.load_local(filepath, self.embeddings)
        logger.info(f"Loaded vectorstore from {filepath}")
        return self.vectorstore
    
    def search(self, query: str, k: int = 5) -> List[Document]:
        if self.vectorstore is None:
            logger.error("Vectorstore is not initialized. Cannot perform search.")
            return []

        return self.vectorstore.similarity_search_with_score(query, k=k)
    
def initialize_vectorstore():
    manager = VectorStoreManager()
    try:
        manger.load_vectorstore()
        logger.info("Vectorstore loaded successfully.")
    except Exception as e:
        logger.warning(f"Failed to load vectorstore: {e}. Creating a new one.")
        loader = CorpusLoader()
        documents = loader.load_all()
        preprocessor = TextPreprocessor()
        processed_docs = preprocessor.preprocess_documents(documents)
        manager.create_vectorstore(processed_docs)
        manager.save_vectorstore()
        logger.info("New vectorstore created and saved.")

    return manager

def main():
    vectorstore_manager = initialize_vectorstore()
    test_query = "¿Cuántos puntos de vida tiene un Arquero?"
    results = vectorstore_manager.search(test_query, k=3)
    print(f"\n✓ Search results for query: '{test_query}'")
    for i, (doc, score) in enumerate(results):
        print(f" Result {i+1}: (Score: {score:.4f})")
        print(f"  Content: {doc.page_content[:200]}...")
        print(f"  Metadata: {doc.metadata}")

if __name__ == "__main__":
    main()
