import os
from pathlib import Path

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

DB_URL = os.getenv("DB_URL", "")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
