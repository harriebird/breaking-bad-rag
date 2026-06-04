from ollama import Client
from sqlmodel import Session, select

from core import config
from models import engine, Paragraph

_llm_client = Client(host=config.OLLAMA_HOST)

def do_search(query):
    if query:
        with Session(engine) as session:
            response = _llm_client.embed(
                model=config.OLLAMA_EMBEDDING_MODEL,
                input=query,
            )

            embed_query = response.embeddings[0]

            paragraphs = session.exec(select(Paragraph).order_by(Paragraph.embedding.l2_distance(embed_query)).limit(5))
            contexts = [paragraph for paragraph in paragraphs]
            return contexts

def do_prompt(query, contexts):
    template = f"""
Use only the provided contexts to answer the question.
Make your answer concise.
If you don't know the answer, just say I don't know.

Contexts:
{"\n".join(context.text for context in contexts)}

Question:
{query}
"""
    response = _llm_client.generate(
        model=config.OLLAMA_LANGUAGE_MODEL,
        prompt=template,
        stream=False
    )
    return response.response

def do_chat(text):
    results = do_search(text)
    response = do_prompt(text, results)
    references = "\n\nReferences:"
    for result in results:
        references += f"\nS{result.season:02d}E{result.episode:02d}: {result.title}\n Link: {result.plot_url}\n"
    response += references
    return response

