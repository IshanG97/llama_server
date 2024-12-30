# Llama 3.2 1B Instruct Server Setup

Local FastAPI server using Llama 3.2 1B Instruct for response generation, accessible via REST API.

Install Required Packages:
`pip install fastapi uvicorn accelerate transformers`

Install PyTorch:
1. Check your system's CUDA version:
   `nvidia-smi`
2. Visit https://pytorch.org/ and install the appropriate version. Example:
   `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`

Run the Server:
`uvicorn serve_llama:app --host 0.0.0.0 --port 8000`
