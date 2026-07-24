# breaking-bad-rag-ollama

Ollama and model installer script for breaking-bad-rag. The current version of this install script works in Linux-based
distributions. Other OS such as MacOS and Windows, are highly encouraged to use the official installer from Ollama and
manually pull the needed models.

## Usage
- `./setup.sh install` - installs Ollama and pull the models needed for this project.
- `./setup.sh updates` - updates Ollama installed in the system.
- `./setup.sh pullmodel` - pulls the `embeddinggemma-300m` and `gemma-3-1b-it` models.
- `./setup.sh uninstall` - removes the models and uninstalls Ollama from the system.
