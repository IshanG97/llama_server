# Llama 3.2 1B Instruct Server Setup

Local FastAPI server using Llama 3.2 1B Instruct for response generation, accessible via REST API.

Install Required Packages:

- Method 1: 
   On Windows: `pip install -r requirements_windows.txt`
   On macOS: `pip install -r requirements_mac.txt`

- Method 2: `pip install fastapi uvicorn accelerate transformers`

You can get access from Meta to download Llama via Meta's HuggingFace repo

Install PyTorch:

1. If you are doing this on a CUDA-accelerated device, check your system's CUDA version: `nvidia-smi`

2. Visit https://pytorch.org/ and install the appropriate version. e.g. `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`

To run the LLM server:

1. Run in  one terminal: `uvicorn serve_llama:app --host 0.0.0.0 --port 8000` 
2. Run in another terminal: `test_llama_remote.py`

If you merely want to test LLM responses without setting up the server, run `test_llama_local.py`


Add as a submodule to parent repo: `git submodule add https://github.com/IshanG97/llama_server.git llama_server`


To update when cloning parent repo for the first time: `git submodule update --init --recursive`
