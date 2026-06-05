import gradio as gr
from sqlmodel import SQLModel

from core import embed, chat

def receive_message(message, history):
    if "/help" in message:
        return "Welcome to Breaking Bad RAG! Here are some commands that will help:\n" \
               "`/help` - displays this help message.\n" \
               "`/start-embedding` - starts embedding the Breaking Bad knowledge base and stores it to a vector DB.\n" \
               "`/clear-embedding` - clears the existing embedding records in the vector DB."

    if "/start-embedding" in message:
        count = embed.count_db_content()
        if count > 0:
            return f"Can't start embedding. There are {count} existing records.\n" \
                   "Try `/clear-embedding` first to clear all the existing records."

        success = embed.embed()

        if success:
            return "Embedding and storage to vector DB was successful!"
        return "Embedding and storage to vector DB was not successful!"

    response = chat.do_chat(message)
    return response

def clear_metadata():
    SQLModel.metadata.clear()

with gr.ChatInterface(fn=receive_message, examples=["/help"], title="Breaking Bad RAG") as chat_app:
    chat_app.load(fn=clear_metadata)

chat_app.launch()
