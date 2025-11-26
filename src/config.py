import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CORPUS_DIR = DATA_DIR / "corpus/es"
VECTORSTORE_DIR = DATA_DIR / "vectorstore"
LOGS_DIR = BASE_DIR / "logs"

# Model Configuration
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTORSTORE_TYPE = os.getenv("VECTORSTORE_TYPE", "faiss")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = LOGS_DIR / "chatbot.log"

# LangChain Configuration
LANGCHAIN_VERBOSE = os.getenv("LANGCHAIN_VERBOSE", "false").lower() == "true"
LANGCHAIN_DEBUG = os.getenv("LANGCHAIN_DEBUG", "false").lower() == "true"

# Feature Flags
USE_DOCUMENT_QA_TOOL = os.getenv("USE_DOCUMENT_QA_TOOL", "false").lower() == "true"
USE_FACT_CHECKER = os.getenv("USE_FACT_CHECKER", "false").lower() == "true"

# Agent Configuration
AGENT_MAX_ITERATIONS = 10
AGENT_TIMEOUT_SECONDS = 30

# Vector Store Configuration
FAISS_INDEX_FILE = VECTORSTORE_DIR / "index.faiss"
METADATA_FILE = VECTORSTORE_DIR / "metadata.pkl"
print(f"✓ Config loaded from {BASE_DIR}")
