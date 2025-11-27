from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List
from src.config import EMBEDDINGS_MODEL
from src.utils.logger import get_logger


logger = get_logger(__name__)

class EmbeddingsManager:
    def __init__(self, model_name: str = EMBEDDINGS_MODEL):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        logger.info(f"Loaded embeddings model: {model_name}")

    def embed_text(self, text: str) -> np.ndarray:
        embedding = self.model.encode(text, convert_to_tensor=False)
        return embedding

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        logger.info(f"Generating embeddings for {len(texts)} texts...")
        embeddings = self.model.encode(texts, convert_to_tensor=False)
        logger.info(f"Generated {len(embeddings)} embeddings")
        return embeddings
    
    def similarity(self, text1: str, text2: str) -> float:
        from sklearn.metrics.pairwise import cosine_similarity
        emb1 = self.embed_text(text1).reshape(1, -1)
        emb2 = self.embed_text(text2).reshape(1, -1)
        return cosine_similarity(emb1, emb2)[0][0]

def main():
    logger.info("Downloading embeddings model...")
    manager = EmbeddingsManager()
    test_text = "¿Cuánto HP tiene el Arquero?"
    embedding = manager.embed_text(test_text)
    print(f"\n✓ Model ready!")
    print(f" Text: '{test_text}'")
    print(f" Embedding shape: {embedding.shape}")
    print(f" First 10 values: {embedding[:10]}")

if __name__ == "__main__":
    main()
    