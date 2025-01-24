from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from setup import setup_llm
from vllm import SamplingParams

# Initialize the FastAPI app
app = FastAPI()

# Load the vLLM model when the server starts
print("Initializing the vLLM model...")
llm = setup_llm()

if not llm:
    raise RuntimeError("Failed to initialize vLLM. Ensure model is correctly configured.")

# Define the input format for the API
class Query(BaseModel):
    conversation_history: list

@app.get("/health")
def health_check():
    return {'status': 'ok'}

@app.post("/gen_response")
async def gen_response(query: Query):
    """
    Accepts conversation history and generates a response.
    """
    try:
        # Configure sampling parameters
        sampling_params = SamplingParams(
            temperature=1.0,
            top_p=0.9,
            max_tokens=256,
            n=1,  # num_return_sequences
        )

        # vLLM expects a string input, so we need to format the conversation history
        prompt = " ".join(query.conversation_history)  # You might want to format this differently
        
        # Generate response
        outputs = llm.generate(prompt, sampling_params)
        
        # Extract the generated text from the response
        reply = outputs[0].outputs[0].text
        
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)