import gradio as gr
from sqlmodel import SQLModel

from core import embed, chat

def receive_message(message, history):
    if "/help" in message:
        return "Welcome to Breaking Bad RAG! Here are some commands that will help you navigate this app:\n" \
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

    if "/clear-embedding" in message:
        count = embed.count_db_content()
        if count < 1:
            return f"Can't start clearing. There are no existing records.\n" \
                   "Try `/start-embedding` first to add embedding records to the vector DB."

        success = embed.clear_embed_store()

        if success:
            return "Clearing of embedding storage was successful!"
        return "Clearing of embedding storage as not successful!"

    count = embed.count_db_content()
    if count < 1:
        return f"Can't answer you with the information from the knowledge base.\n" \
               "There's existing records stored in the vector DB yet.\n" \
               "Try `/start-embedding` first to add embedding records to the vector DB."

    response = chat.do_chat(message)
    return response

def clear_metadata():
    SQLModel.metadata.clear()

with gr.ChatInterface(fn=receive_message, examples=["/help"], title="Breaking Bad RAG") as chat_app:
    chat_app.load(fn=clear_metadata)

chat_app.launch()
