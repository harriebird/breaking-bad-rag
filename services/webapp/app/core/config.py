import os
from pathlib import Path

OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL")
OLLAMA_LANGUAGE_MODEL = os.getenv("OLLAMA_LANGUAGE_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

DB_URL = os.getenv("DB_URL", "")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
