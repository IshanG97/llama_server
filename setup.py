from vllm import LLM, SamplingParams

def setup_llm(model_id="meta-llama/Llama-3.2-1B-Instruct", dtype="bfloat16", gpu_memory_utilization=0.9):
    print("Ensure you have logged into huggingface-cli (with a token) before accessing gated models.")

    try:
        # vLLM provides direct model loading - no separate tokenizer needed
        llm = LLM(
            model=model_id,
            dtype=dtype,  # vLLM uses string dtype instead of torch.dtype
            gpu_memory_utilization=gpu_memory_utilization,
            # Optional parameters you might want:
            # tensor_parallel_size=1,  # For multi-GPU
            # max_num_batched_tokens=4096,
            # quantization="awq"  # If you want to use quantization
        )
        
        print("Setup complete. The LLM is ready to use!")
        return llm
    except Exception as e:
        print(f"Error initializing vLLM: {e}")
        return None