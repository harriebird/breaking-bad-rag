import re

from datasets import load_dataset
import config

def split_paragraphs(plots):
    paragraphs = []
    for plot in plots:
        chunks = re.split(r"\n*\n", plot["plot"])
        paragraph = {}
        paragraph["season"] = plot["season"]
        paragraph["episode"] = plot["episode"]
        paragraph["title"] = plot["title"]
        paragraph["text"] = plot["text"]
        for chunk in chunks:
            clean = chunk.strip()
            if len(clean) > 30:
                paragraphs.append(clean)
    return paragraphs

plots_dataset = load_dataset(f"{config.PROJECT_ROOT}/data/dataset.csv")