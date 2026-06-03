import os

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

DB_URL = os.getenv("DB_URL", "")
