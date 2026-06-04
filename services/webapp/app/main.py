import gradio as gr
from sqlmodel import SQLModel

from core import embed, chat

def receive_message(message, history):
    if "/start-embedding" in message:
        success = embed.embed()
        if success:
            return "Embedding and storage to vector DB was successful!"
        return "Embedding and storage to vector DB was not successful!"

    response = chat.do_chat(message)
    return response

def clear_metadata():
    SQLModel.metadata.clear()

with gr.ChatInterface(fn=receive_message, examples=["/start-embedding"], title="Breaking Bad RAG") as chat_app:
    chat_app.load(fn=clear_metadata)

chat_app.launch()
