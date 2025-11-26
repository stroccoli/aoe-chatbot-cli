import os
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any
from langchain.schema import Document
from src.config import CORPUS_DIR
from src.utils.logger import get_logger


logger = get_logger(__name__)

class CorpusLoader:
    def __init__(self, corpus_dir: Path = CORPUS_DIR):
        self.corpus_dir = corpus_dir
        self.documents = []

    def load_markdown(self, filepath: Path) -> List[Document]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            doc = Document(
                page_content=content,
                metadata={'source': filepath.name, 'type': 'markdown'}
            )
            logger.info(f"Loaded markdown: {filepath.name} ({len(content)} chars)")
            return [doc]
        except Exception as e:
            logger.error(f"Error loading markdown {filepath}: {e}")
            return []

    def load_csv(self, filepath: Path) -> List[Document]:
        try:
            df = pd.read_csv(filepath)
            documents = []
            for idx, row in df.iterrows():
                content = self._row_to_text(row, filepath.stem)
                doc = Document(
                    page_content=content,
                    metadata={
                        'source': filepath.name,
                        'type': 'csv',
                        'index': idx,
                        'name': row.get('name', f"Item {idx}")
                    }
                )
                documents.append(doc)
            
            logger.info(f"Loaded CSV: {filepath.name} ({len(documents)} rows)")
            return documents
        except Exception as e:
            logger.error(f"Error loading CSV {filepath}: {e}")
            return []

    def load_all(self) -> List[Document]:
        all_documents = []
        if not self.corpus_dir.exists():
            logger.error(f"Corpus directory does not exist: {self.corpus_dir}")
            return all_documents
            

        for md_file in self.corpus_dir.glob("*.md"):
            all_documents.extend(self.load_markdown(md_file))
        
        for csv_file in self.corpus_dir.glob("*.csv"):
            all_documents.extend(self.load_csv(csv_file))

        self.documents = all_documents
        logger.info(f"Total documents loaded: {len(self.documents)}")
        return self.documents
