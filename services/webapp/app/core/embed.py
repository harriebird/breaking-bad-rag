import re

from ollama import Client
import pandas as pd
from sqlmodel import Session

from core import config
from models import engine, Paragraph

_llm_client = Client(host=config.OLLAMA_HOST)

def split_plots_to_paragraphs(df):
    paragraphs = []
    for plot in df.itertuples():
        chunks = re.split(r"\n*\n", plot.plot)
        for chunk in chunks:
            clean = chunk.strip()
            paragraph = {
                "season": plot.season,
                "episode": plot.episode,
                "title": plot.title,
                "link": plot.link,
                "text": clean
            }
            if len(clean) > 30:
                paragraphs.append(paragraph)
    return paragraphs

def load_dataset():
    plots_df = pd.read_csv(f"{config.PROJECT_ROOT}/data/dataset.csv")
    return plots_df

def embed():
    with Session(engine) as session:
        plots_df = load_dataset()
        paragraphs = split_plots_to_paragraphs(plots_df)
        for paragraph in paragraphs:
            new_paragraph = Paragraph()
            response = _llm_client.embed(
                model=config.OLLAMA_EMBEDDING_MODEL,
                input=paragraph["text"],
            )
            new_paragraph.season = paragraph["season"]
            new_paragraph.episode = paragraph["episode"]
            new_paragraph.title = paragraph["title"]
            new_paragraph.plot_url = paragraph["link"]
            new_paragraph.text = paragraph["text"]
            new_paragraph.embedding = response.embeddings[0]
            session.add(new_paragraph)
            session.commit()
            print(f"S{paragraph["season"]:02d}E{paragraph["episode"]:02d} was successfully embedded!")
        return True
