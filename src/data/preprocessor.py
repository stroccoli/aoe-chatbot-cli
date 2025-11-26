import re
from typing import List
from langchain.schema import Document
from src.utils.logger import get_logger

logger = get_logger(__name__)

class TextPreprocessor:
    @staticmethod
    def normalize_text(text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.,!?;]', '', text)
        return text.strip()

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        words = text.split()
        chunks = []
        start = 0
        while start < len(words):
            end = min(start + chunk_size, len(words))
            chunk = ' '.join(words[start:end])
            chunks.append(chunk)
            start += chunk_size - overlap
        return chunks
    
    @staticmethod
    def preprocess_documents(documents: List[Document]) -> List[Document]:
        preprocessed_docs = []
        for doc in documents:
            normalized_text = TextPreprocessor.normalize_text(doc.page_content)
            chunks = TextPreprocessor.chunk_text(normalized_text)
            for i, chunk in enumerate(chunks):
                new_metadata = doc.metadata.copy()
                new_metadata['chunk_index'] = i
                preprocessed_docs.append(Document(page_content=chunk, metadata=new_metadata))
        logger.info(f"Preprocessed {len(documents)} documents into {len(preprocessed_docs)} chunks.")
        return preprocessed_docs

def main():
    from src.data.loader import CorpusLoader
    loader = CorpusLoader()
    docs = loader.load_all()
    preprocessor = TextPreprocessor()
    cleaned_docs = preprocessor.preprocess_documents(docs)
    print(f"\n✓ Preprocessed {len(cleaned_docs)} documents")
    print(f"\nOriginal first doc: {docs[0].page_content[:100]}")
    print(f"\nCleaned first doc: {cleaned_docs[0].page_content[:100]}")

if __name__ == "__main__":
    main()