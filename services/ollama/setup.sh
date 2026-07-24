#!/bin/bash

case $1 in
  update)
    curl -fsSL https://ollama.com/install.sh | sh
    ;;
  install)
    ./setup.sh update
    sudo cp ollama.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl stop ollama
    sudo systemctl start ollama
    ./setup.sh pullmodel
    ;;
  pullmodel)
    ollama pull hf.co/unsloth/embeddinggemma-300m-GGUF:Q4_0
    ollama pull hf.co/unsloth/gemma-3-1b-it-GGUF:Q4_K_M
    ;;
  uninstall)
    ollama rm hf.co/unsloth/embeddinggemma-300m-GGUF:Q4_0
    ollama rm hf.co/unsloth/gemma-3-1b-it-GGUF:Q4_K_M
    sudo systemctl stop ollama
    sudo systemctl disable ollama
    sudo rm /etc/systemd/system/ollama.service
    sudo rm -r $(which ollama | tr 'bin' 'lib')
    sudo rm $(which ollama)
    ;;
  *)
    echo "Usage:
    ./setup.sh install - installs Ollama and pull the models needed for this project.
    ./setup.sh updates - updates Ollama installed in the system.
    ./setup.sh pullmodel - pulls the embeddinggemma-300m and gemma-3-1b-it models.
    ./setup.sh uninstall - removes the models and uninstalls Ollama from the system.
    "
    ;;
esac