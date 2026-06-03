import gradio as gr

def receive_message(message, history):
    return message

demo = gr.ChatInterface(fn=receive_message, examples=["/start-embedding"], title="Breaking Bad RAG")

demo.launch()
