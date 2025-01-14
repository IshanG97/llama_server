# Llama 3.2 1B Instruct Server Setup

Local FastAPI server using Llama 3.2 1B Instruct for response generation, accessible via REST API.

Install Required Packages:

- Method 1: 
   On Windows: `pip install -r requirements_windows.txt`
   On macOS: `pip install -r requirements_mac.txt`

- Method 2: `pip install fastapi uvicorn accelerate transformers`


Install PyTorch:

1. Check your system's CUDA version: `nvidia-smi`

2. Visit https://pytorch.org/ and install the appropriate version. e.g. `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`


Run the Server: `uvicorn serve_llama:app --host 0.0.0.0 --port 8000`


Add as a submodule to parent repo: `git submodule add https://github.com/IshanG97/llama_server.git llama_server`


To update when cloning parent repo for the first time: `git submodule update --init --recursive`
