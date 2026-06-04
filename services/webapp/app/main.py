import gradio as gr

from core import embed

def receive_message(message, history):
    if "/start-embedding" in message:
        success = embed.embed()
        if success:
            return "Embedding and storage to vector DB was successful!"
        return "Embedding and storage to vector DB was not successful!"

    return message


demo = gr.ChatInterface(fn=receive_message, examples=["/start-embedding"], title="Breaking Bad RAG")

demo.launch()
