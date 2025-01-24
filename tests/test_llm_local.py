import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from setup import setup_llm
from vllm import SamplingParams

# Step 1: Load the vLLM model
print("Initializing vLLM...")
llm = setup_llm()

if not llm:
    print("Failed to initialize vLLM. Exiting.")
else:
    print("vLLM initialized. Ready for input!")

    # Step 2: Initialize conversation history
    conversation_history = [
        {"role": "system", "content": "You are a pirate chatbot. Respond in pirate speak in 50 words or less. Make controversial statements."},
    ]
    
    # Function to format conversation history
    def format_conversation(history):
        formatted = ""
        for msg in history:
            if msg["role"] == "system":
                formatted += f"System: {msg['content']}\n"
            elif msg["role"] == "user":
                formatted += f"User: {msg['content']}\n"
            elif msg["role"] == "assistant":
                formatted += f"Assistant: {msg['content']}\n"
        return formatted

    # Set up sampling parameters
    sampling_params = SamplingParams(
        temperature=1.0,
        top_p=0.9,
        max_tokens=256,
        n=1,
    )

    # Step 3: Accept new inputs dynamically
    while True:
        input_text = input("Enter your text (or type 'exit' to quit): ")
        if input_text.lower() == "exit":
            print("Exiting...")
            break

        # Append the user's input to the conversation history
        conversation_history.append({"role": "user", "content": input_text})

        # Generate a reply
        try:
            # Format the conversation history into a prompt
            prompt = format_conversation(conversation_history)
            
            # Generate response using vLLM
            outputs = llm.generate(prompt, sampling_params)
            
            # Extract the generated text
            reply = outputs[0].outputs[0].text
            print("Generated Reply:", reply)

            # Add the assistant's reply to the conversation history
            conversation_history.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"Error during text generation: {e}")